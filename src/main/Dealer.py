from src.main.Player import Player

class Dealer(Player):

    def __init__(self):
        super().__init__("dealer", None, None)

    def getfaceUpCard(self):
        return self.cards[1]

