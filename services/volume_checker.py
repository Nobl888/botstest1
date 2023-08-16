```python
from models.token import Token
from api.dextools import DextoolsAPI
from api.dexscreener import DexscreenerAPI

class VolumeChecker:
    def __init__(self, api_key):
        self.dextools_api = DextoolsAPI(api_key)
        self.dexscreener_api = DexscreenerAPI(api_key)

    def get_tokens_with_growing_volume(self):
        dextools_tokens = self.dextools_api.get_all_tokens()
        dexscreener_tokens = self.dexscreener_api.get_all_tokens()

        growing_volume_tokens = []

        for token in dextools_tokens:
            if self.is_volume_growing(token):
                growing_volume_tokens.append(token)

        for token in dexscreener_tokens:
            if self.is_volume_growing(token):
                growing_volume_tokens.append(token)

        return growing_volume_tokens

    def is_volume_growing(self, token):
        volume_data = token.get_volume_data()
        if len(volume_data) < 2:
            return False

        return volume_data[-1] > volume_data[-2]
```