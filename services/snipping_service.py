```python
from models.token import Token
from api.dextools import DextoolsAPI
from api.dexscreener import DexscreenerAPI

class SnippingService:
    def __init__(self, dextools_api: DextoolsAPI, dexscreener_api: DexscreenerAPI):
        self.dextools_api = dextools_api
        self.dexscreener_api = dexscreener_api

    def snip_token(self, token: Token):
        # Snip token from Dextools
        if token.source == 'dextools':
            response = self.dextools_api.snip_token(token.id)
            if response.status_code == 200:
                print(f'TOKEN_SNIPPED: {token.name} from Dextools')
            else:
                print(f'ERROR_SNIPPING_TOKEN: {token.name} from Dextools')

        # Snip token from Dexscreener
        elif token.source == 'dexscreener':
            response = self.dexscreener_api.snip_token(token.id)
            if response.status_code == 200:
                print(f'TOKEN_SNIPPED: {token.name} from Dexscreener')
            else:
                print(f'ERROR_SNIPPING_TOKEN: {token.name} from Dexscreener')

        else:
            print(f'UNKNOWN_SOURCE: {token.source} for token {token.name}')
```