
import unittest
from src.exceptions.BrokeException import BrokeException
from src.main.Wallet import Wallet

class TestWallet(unittest.TestCase):
    def test_wallet_creation(self):
        wallet = Wallet(0)
        self.assertEqual(wallet.total, 0)
    
    def test_wallet_addMoney(self):
        wallet = Wallet(200)
        wallet.addMoney(500)
        self.assertEqual(wallet.total, 700)

    def test_wallet_loseMoney(self):
        wallet = Wallet(200)

        with self.assertRaises(BrokeException) as context:
            wallet.loseMoney(300)

        self.assertTrue('You are broke. Wallet total: -100' in str(context.exception))

if __name__ == '__main__':
    unittest.main()