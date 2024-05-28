import unittest
from src.main.Wallet import Wallet
from src.utils.PlayUtils import playWithFullDeck
from src.utils.StrategyUtils import dealer_strategy, player_strategy_hardTotal, player_strategy_hardSoftTotal

class TestStrategy(unittest.TestCase):

    def testPlay_dealer_strategy(self):
        results = {
            "peasant_score": [],
            "dealer_score": [],
            "winner": [],
            "round": [],
            "peasant_wallet": []
        }
        wallet = Wallet(100)
        bet = 25
        numOfDecks = 1
        round = 2

        playWithFullDeck(dealer_strategy, wallet, bet, numOfDecks, round, results)
        # print(results)  

    def testPlay_HT_strategy(self):
        results = {
            "peasant_score": [],
            "dealer_score": [],
            "winner": [],
            "round": [],
            "peasant_wallet": []
        }
        wallet = Wallet(100)
        bet = 25
        numOfDecks = 1
        round = 2

        playWithFullDeck(player_strategy_hardTotal, wallet, bet, numOfDecks, round, results, print_enabled= False)
        # print(results)        

    def testPlay_HST_strategy(self):
        results = {
            "peasant_score": [],
            "dealer_score": [],
            "winner": [],
            "round": [],
            "peasant_wallet": []
        }
        wallet = Wallet(100)
        bet = 25
        numOfDecks = 1
        round = 2

        playWithFullDeck(player_strategy_hardSoftTotal, wallet, bet, numOfDecks, round, results, print_enabled= False)
        print(results)        

if __name__ == '__main__':
    unittest.main()