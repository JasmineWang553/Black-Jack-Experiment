import random

class Card:
    def __init__(self, numOfDecks) -> None:
        self.deck = self.createDeck(numOfDecks)
    
    def createDeck(self, numOfDecks):
        deck = []
        deck = ["A" for i in range(4 * numOfDecks)]

        for i in range(2, 14):
            if i >= 11:
                for j in range(4 * numOfDecks):
                    deck.append(10) 
            else:
                for j in range(4 * numOfDecks):
                    deck.append(i) 

        random.shuffle(deck)
        return deck
    
    def drawRandomCard(self):
        if len(self.deck) == 0:
            raise Exception("deck is finished")
            
        return self.deck.pop()
        

