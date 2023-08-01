import requests
from models.token import Token
import config

class DexscreenerAPI:
    def __init__(self):
        self.base_url = config.DEXSCREENER_BASE_URL
        self.api_key = config.DEXSCREENER_API_KEY

    def get_tokens_with_growing_volume(self):
        response = requests.get(f"{self.base_url}/tokens?api_key={self.api_key}&volume=growing")
        data = response.json()

        tokens = []
        for item in data:
            token = Token(item['symbol'], item['address'], item['volume'])
            tokens.append(token)

        return tokens

    def snip_token(self, token):
        response = requests.post(f"{self.base_url}/snip?api_key={self.api_key}", data=token.to_dict())
        return response.status_code == 200
