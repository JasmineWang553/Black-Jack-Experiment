from src.main.Card import Card
from src.main.Player import Player
from src.main.Dealer import Dealer
from src.main.Wallet import Wallet
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from src.utils.StrategyUtils import drawCard, dealer_strategy, player_strategy_hardTotal
from src.exceptions.BrokeException import BrokeException

def getWinner(player1, player2):
    if player1.score <= 21 and player2.score <= 21:

        if player1.score > player2.score:
            winner = player1
            loser = player2
        elif player2.score > player1.score:
            winner = player2
            loser = player1
        elif player2.score == player1.score:
            return None, None
        
    return winner, loser

def result_append(winner, loser, round, results, print_enabled=False):
    if print_enabled:
        print(f"Winner is: {winner.name}; Winner Score: {winner.score} & Loser Score {loser.score}")
    
    if winner.name != "dealer":
        winner.wallet.addMoney(winner.bet)
        results["peasant_wallet"].append( winner.wallet.total)
    if loser.name != "dealer":
        loser.wallet.loseMoney(loser.bet)
        results["peasant_wallet"].append( loser.wallet.total)

    results["winner"].append(winner.name)
    results["peasant_score"].append(winner.score if winner.name == "peasant" else loser.score)
    results["dealer_score"].append(winner.score if winner.name == "dealer" else loser.score)
    results['round'].append(round)
    
def playLogic(player_strategy, wallet, bet, deck, round, results, print_enabled=False):
    dealer = Dealer()
    peasant = Player(name="peasant", wallet=wallet, bet=bet) 
    drawCard(deck, peasant)
    drawCard(deck, dealer)
    drawCard(deck, peasant)
    drawCard(deck, dealer)

    player_strategy(deck, peasant, dealer, print_enabled)
    if peasant.bustCheck():
        result_append(winner=dealer, loser=peasant, round=round, results=results)
        return

    dealer_strategy(deck, dealer, None, print_enabled)

    if dealer.bustCheck():
        result_append(winner=peasant, loser=dealer,round=round, results=results)
    else:
        winner, loser = getWinner(dealer, peasant)
        if winner == None and loser == None:
            results["dealer_score"].append(dealer.score)
            results["peasant_score"].append(peasant.score)
            results["winner"].append("tie")
            results["peasant_wallet"].append(peasant.wallet.total)
            results['round'].append(round)
        else:
            result_append(winner, loser, round=round, results=results)

def playWithFullDeck(player_strategy, wallet, bet, numOfDecks, round, results, print_enabled=False):
    if print_enabled:
        print("game start")

    deck = Card(numOfDecks)
    while len(deck.deck) > 0:
        try:
            playLogic(player_strategy, wallet, bet, deck, round, results, print_enabled)
        except BrokeException as e: 
            print(e)
            break
        except Exception as e: 
            if print_enabled:
                print(e)
            break 

    if print_enabled:
        print("game end")
        print(f"NO OF RESULTS: {len(results["winner"])}")    

def iterativePlayWithOneWallet(playerStrategy, startingMoney, bet, numOfDecks, plot_enabled=False):
    results = {
        "peasant_score": [],
        "dealer_score": [],
        "winner": [],
        "peasant_wallet": [],
        "round": []
    }
    bet = bet
    wallet = Wallet(startingMoney)
    numOfDecks = numOfDecks
    round = 0

    for i in range(100):
        playWithFullDeck(playerStrategy, wallet = wallet, bet = bet, numOfDecks=numOfDecks, round=round, results = results)
        round += 1

    results_df = pd.DataFrame(results)
    # print(f"Money Left: {wallet.total}")

    if plot_enabled:
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 5) )
        sns.histplot(results_df.winner, ax=ax1)
        sns.lineplot(data=results_df[["peasant_wallet", "round"]].reset_index(), x="index", y="peasant_wallet", hue="round", ax=ax2)
        results_df[["peasant_wallet", "round"]].groupby("round").mean().plot(legend=False, kind="bar", ax=ax3)

    return results_df, wallet.total