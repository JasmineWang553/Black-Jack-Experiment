class Player:
    def __init__(self, name, wallet, bet):
        self.name = name
        self.cards = []
        self.sumOfCardsExceptA = 0
        self.numberOfA = 0
        self.score = 0
        self.wallet = wallet
        self.bet = bet

    def drawCard(self, card):
        self.cards.append(card)

        if card == 'A':
            self.numberOfA += 1
        else:
            self.sumOfCardsExceptA += card
        
        self.score = self.calculateSum()

    def calculateSum(self):
        total = self.sumOfCardsExceptA

        if self.numberOfA != 0:
            diff = 21 - self.sumOfCardsExceptA

            if (diff < 11) or (diff - 11 < self.numberOfA - 1):
                total += self.numberOfA
            else:
                total += 11 + self.numberOfA - 1
                
        return total
    
    def bustCheck(self):
        currSum = self.calculateSum()
        return currSum > 21

    def containsAinFirst2Cards(self):
        if self.cards[0] == "A" or self.cards[1] == "A":
            return True
        return False
    
    def printStatus(self):
        print(f"Name: {self.name}, Score:{self.score}")
    
