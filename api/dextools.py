import requests
from models.token import Token

class DextoolsAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get_tokens_with_growing_volume(self):
        response = requests.get(f"{self.base_url}/tokens?api_key={self.api_key}")
        response.raise_for_status()
        tokens_data = response.json()
        tokens = [Token(**token_data) for token_data in tokens_data]
        return tokens

    def snip_token(self, token):
        response = requests.post(
            f"{self.base_url}/snip?api_key={self.api_key}",
            json=token.to_dict()
        )
        response.raise_for_status()
        return response.json()