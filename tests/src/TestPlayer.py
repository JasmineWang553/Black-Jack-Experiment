import unittest
from src.main.Player import Player
from src.main.Wallet import Wallet

class TestPlayer(unittest.TestCase):
    def test_player_creation(self):
        player = Player(name="peasant", wallet=Wallet(500), bet=10) 
        self.assertIsInstance(player.cards, list)
        self.assertEqual(len(player.cards), 0)
    
    def test_player_draw_card_1(self):
        player = Player(name="peasant", wallet=Wallet(500), bet=10) 
        player.drawCard(10)
        self.assertEqual(player.sumOfCardsExceptA, 10)
        self.assertEqual(player.numberOfA, 0)

    def test_player_draw_card_2(self):
        player = Player(name="peasant", wallet=Wallet(500), bet=10) 
        player.drawCard(10)
        player.drawCard("A")
        player.drawCard("A")
        player.drawCard("A")

        self.assertEqual(player.numberOfA, 3)
        self.assertEqual(player.score, 13)
        self.assertTrue(player.containsAinFirst2Cards())
        self.assertFalse(player.bustCheck())
    
    def test_player_draw_card_3(self):
        player = Player(name="peasant", wallet=Wallet(500), bet=10) 
        player.drawCard(8)
        player.drawCard("A")
        player.drawCard("A")
        player.drawCard("A")

        self.assertEqual(player.numberOfA, 3)
        self.assertEqual(player.score, 21)
        self.assertTrue(player.containsAinFirst2Cards())
        self.assertFalse(player.bustCheck())

    def test_player_draw_card_4(self):
        player = Player(name="peasant", wallet=Wallet(500), bet=10) 
        player.drawCard(5)
        player.drawCard("A")

        self.assertEqual(player.numberOfA, 1)
        self.assertEqual(player.score, 16)
        self.assertTrue(player.containsAinFirst2Cards())
        self.assertFalse(player.bustCheck())

    def test_player_draw_card_5(self):
        player = Player(name="peasant", wallet=Wallet(500), bet=10) 
        player.drawCard("A")
        player.drawCard(4)
        player.drawCard("A")
        player.drawCard(5)

        self.assertEqual(player.numberOfA, 2)
        self.assertEqual(player.score, 21)
        self.assertTrue(player.containsAinFirst2Cards())
        self.assertFalse(player.bustCheck())

    def test_player_draw_card_6(self):
        player = Player(name="peasant", wallet=Wallet(500), bet=10) 
        player.drawCard("A")
        player.drawCard(4)
        player.drawCard("A")
        player.drawCard(8)
        player.drawCard("A")
        player.drawCard(4)

        self.assertEqual(player.numberOfA, 3)
        self.assertEqual(player.score, 19)
        self.assertTrue(player.containsAinFirst2Cards())
        self.assertFalse(player.bustCheck())

    def test_player_bustCheck(self):
        player = Player(name="peasant", wallet=Wallet(500), bet=10) 
        player.drawCard(10)
        player.drawCard(4)
        player.drawCard(8)

        self.assertEqual(player.numberOfA, 0)
        self.assertEqual(player.score, 22)
        self.assertFalse(player.containsAinFirst2Cards())
        self.assertTrue(player.bustCheck())
        

if __name__ == '__main__':
    unittest.main()