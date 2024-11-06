import pytest
from unittest.mock import patch, Mock
import requests
#import MpesaAuth class from auth module

@pytest.fixture
def mpesa_auth():
    consumer_secret = "test_consumer_secret"
    consumer_key = "test_consumer_key"
    # return instance of MPesaAuth class
    # return MpesaAuth(consumer_secret, consumer_key)
    

@patch('mpesa_c2b.auth.requests.get')
def test_successful_token_retrieval(mock_get, mpesa_auth):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'access_token': 'test_token', 'expires_in': 3600}
    mock_get.return_value = mock_response

    token = mpesa_auth.get_access_token()
    assert token == 'test_token'
    

@patch('mpesa_c2b.auth.requests.get')
def test_invalid_credentials(mock_get, mpesa_auth):
    mock_response = Mock()
    mock_response.status_code = 401
    mock_response.json.return_value = {'errorCode': 'test_error_code', 'errorMessage': 'test_error_message'}
    mock_get.return_value = mock_response
    
    with pytest.raises(Exception) as e:
        mpesa_auth.get_access_token()
    assert str(e.value) == "test_error_message"
    
@patch('mpesa_c2b.auth.requests.get')
def test_network_error_handling(mock_get, mpesa_auth):
    # Simulate a network error
    mock_get.side_effect = requests.exceptions.ConnectionError

    with pytest.raises(Exception) as e:
        mpesa_auth.get_access_token()
    assert str(e.value) == "Network error" 
    


