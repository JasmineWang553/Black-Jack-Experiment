import numpy as np


def drawCard(deck, player, print_enabled=False):
    cardDrawn = deck.drawRandomCard()
    if print_enabled:
        print("Card Drawn -> " + str(cardDrawn))
    player.drawCard(cardDrawn)

def dealer_strategy(deck, player, dealer, print_enabled):
    while player.score < 17:
        drawCard(deck, player, print_enabled)
        if player.bustCheck():
            break

def player_strategy_hardTotal(deck, player, dealer, print_enabled):
    while player.score < 17:
        move = hard_totals[player.score][dealer.getfaceUpCard() if dealer.getfaceUpCard() != "A" else 11]
        if print_enabled:
            print("Move -> "  + str(move))
        match move:
            case 0:
                break
            case 1:
                drawCard(deck, player, print_enabled)
            case 2: 
                player.bet *= 2
                drawCard(deck, player, print_enabled)
                break

def player_strategy_hardSoftTotal(deck, player, dealer, print_enabled=False):
    if player.containsAinFirst2Cards() and len(player.cards) == 2:
        move = soft_totals[player.score][dealer.getfaceUpCard() if dealer.getfaceUpCard() != "A" else 11]
        match move:
            case 0:
                pass
            case 1:
                drawCard(deck, player)
            case 2: 
                player.bet *= 2
                drawCard(deck, player)

    
    player_strategy_hardTotal(deck, player, dealer, print_enabled)
    

# Actions: 0 - Stand, 1 - Hit, 2 - Double Down, 3 - Split
hard_totals = {
    2: [1]*12,
    3: [1]*12,
    4: [1]*12,
    5: [1]*12,
    6: [1]*12,
    7: [1]*12,
    8: [1]*12,
    9: [1]*3 + [2]*4 + [1]*5,
    10: [2]*10 + [0]*2,
    11: [2]*12,
    12: [1]*4 + [0]*3 + [1]*5,
    13: [0]*7 + [1]*5,
    14: [0]*7 + [1]*5,
    15: [0]*7 + [1]*5,
    16: [0]*7 + [1]*5,
    17: [0]*12,
    18: [0]*12,
    19: [0]*12,
    20: [0]*12,
    21: [0]*12
}

soft_totals = {
    13: [0]*2 + [1]*3 + [2]*2 + [1]*5,
    14: [0]*2 + [1]*3 + [2]*2 + [1]*5,
    15: [0]*2 + [1]*2 + [2]*3 + [1]*5,
    16: [0]*2 + [1]*2 + [2]*3 + [1]*5,
    17: [0]*2 + [1]*1 + [2]*4 + [1]*5,
    18: [0]*3 + [2]*4 + [0]*2 + [1]*3,
    19: [0]*12,
    20: [0]*12,
    21: [0]*12
}
