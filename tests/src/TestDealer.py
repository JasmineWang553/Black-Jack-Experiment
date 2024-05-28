import unittest
import random
from src.main.Dealer import Dealer

class TestDealer(unittest.TestCase):
    def test_dealer_creation(self):
        dealer = Dealer()
        self.assertIsInstance(dealer.cards, list)
        self.assertEqual(len(dealer.cards), 0)
    
    def test_dealer_faceUpCard(self):
        dealer = Dealer()
        random.seed(10)
        dealer.drawCard(10)
        dealer.drawCard('A')
        self.assertIsInstance(dealer.cards, list)
        self.assertEqual(len(dealer.cards), 2)
        self.assertEqual(dealer.getfaceUpCard(), "A")

if __name__ == '__main__':
    unittest.main()