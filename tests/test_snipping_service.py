import unittest
from services.snipping_service import SnippingService
from models.token import Token

class TestSnippingService(unittest.TestCase):
    def setUp(self):
        self.snipping_service = SnippingService()
        self.token = Token('0x123', 'TestToken', 100)

    def test_snip_token(self):
        result = self.snipping_service.snip_token(self.token)
        self.assertEqual(result, "TOKEN_SNIPPED")

    def test_snip_token_fail(self):
        self.token = None
        result = self.snipping_service.snip_token(self.token)
        self.assertEqual(result, "TOKEN_SNIPPING_FAILED")

if __name__ == '__main__':
    unittest.main()