```python
import config
from models.token import Token
from api.dextools import DextoolsAPI
from api.dexscreener import DexscreenerAPI
from services.volume_checker import VolumeChecker
from services.snipping_service import SnippingService

class Bot:
    def __init__(self):
        self.dextools_api = DextoolsAPI(config.DEXTOOLS_API_KEY)
        self.dexscreener_api = DexscreenerAPI(config.DEXSCREENER_API_KEY)
        self.volume_checker = VolumeChecker()
        self.snipping_service = SnippingService()

    def get_tokens_with_growing_volume(self):
        tokens = self.dextools_api.get_all_tokens()
        tokens.extend(self.dexscreener_api.get_all_tokens())
        return self.volume_checker.get_tokens_with_growing_volume(tokens)

    def snip_token(self, token: Token):
        return self.snipping_service.snip_token(token)

    def run_bot(self):
        while True:
            tokens_with_growing_volume = self.get_tokens_with_growing_volume()
            for token in tokens_with_growing_volume:
                snip_result = self.snip_token(token)
                if snip_result:
                    print(f'TOKEN_SNIPPED: {token.symbol}')
                else:
                    print(f'FAILED_TO_SNIP: {token.symbol}')

if __name__ == "__main__":
    bot = Bot()
    bot.run_bot()
```