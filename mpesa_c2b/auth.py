import os
import requests
from requests.auth import HTTPBasicAuth

class MpesaAuth:
    def __init__(self, consumer_secret, consumer_key):
        self.consumer_secret = consumer_secret
        self.consumer_key = consumer_key
        self.base_url = os.getenv('AUTH_BASE_URL')
        
        
    def get_access_token(self):
        """
        Get access token from the Mpesa API
        """
        token_url = f"{self.base_url}/oauth/v1/generate?grant_type=client_credentials"
        try:
            response = requests.get(token_url, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
            if response.status_code == 200:
                return response.json().get('access_token')
            else:
                error_message = response.json().get('error_message', 'Failed to obtain access token')
                raise Exception(error_message)
        except requests.exceptions.ConnectionError:
            raise Exception("Network error")