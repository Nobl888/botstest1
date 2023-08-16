import unittest
from bot import CryptoBot
from models.token import Token
from services.volume_checker import VolumeChecker
from services.snipping_service import SnippingService

class TestCryptoBot(unittest.TestCase):

    def setUp(self):
        self.bot = CryptoBot()

    def test_run_bot(self):
        self.bot.run_bot()
        self.assertTrue(self.bot.is_running)

    def test_get_tokens_with_growing_volume(self):
        tokens = self.bot.get_tokens_with_growing_volume()
        for token in tokens:
            self.assertIsInstance(token, Token)
            self.assertTrue(VolumeChecker.is_volume_growing(token))

    def test_snip_token(self):
        token = Token('TestToken', '0x123', 100)
        self.bot.snip_token(token)
        self.assertIn(token, SnippingService.snipped_tokens)

if __name__ == '__main__':
    unittest.main()