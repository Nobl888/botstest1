import unittest
from services.volume_checker import VolumeChecker
from models.token import Token

class TestVolumeChecker(unittest.TestCase):

    def setUp(self):
        self.volume_checker = VolumeChecker()
        self.token = Token('0x123', 'TestToken')

    def test_get_tokens_with_growing_volume(self):
        result = self.volume_checker.get_tokens_with_growing_volume()
        self.assertIsInstance(result, list)
        for token in result:
            self.assertIsInstance(token, Token)

    def test_check_token_volume_growth(self):
        result = self.volume_checker.check_token_volume_growth(self.token)
        self.assertIsInstance(result, bool)

if __name__ == '__main__':
    unittest.main()