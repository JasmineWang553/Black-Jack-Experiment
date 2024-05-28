
import unittest
import random
from src.main.Card import Card

class TestCard(unittest.TestCase):
    def test_create_deck(self):
        deck = Card(1)
        self.assertIsInstance(deck.deck, list)
        self.assertEqual(len(deck.deck), 52)

    def test_draw_random_card(self):
        deck = Card(1)
        random.seed(10)
        deck.drawRandomCard()
        self.assertEqual(len(deck.deck), 51)
        deck.drawRandomCard()
        self.assertEqual(len(deck.deck), 50)
        

if __name__ == '__main__':
    unittest.main()