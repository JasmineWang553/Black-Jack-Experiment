import sys
from src.exceptions.BrokeException import BrokeException

class Wallet():
    def __init__(self, total) -> None:
        self.total = total

    def addMoney(self, money):
        self.total += money

    def loseMoney(self, money):
        self.total -= money

        if self.total <= 0:
            raise BrokeException("You are broke. Wallet total: " + str(self.total))


    def printWallet(self):
        print("My wallet: " + self.total)