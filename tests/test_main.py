import unittest
from unittest.mock import patch
from main import run_bot

class TestMain(unittest.TestCase):

    @patch('bot.Bot.run')
    def test_run_bot(self, mock_run):
        run_bot()
        mock_run.assert_called_once()

if __name__ == '__main__':
    unittest.main()