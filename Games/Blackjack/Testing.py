import random
#from Blackjack import *
from Functions import blackjack
sets= []
'''def random_card():
    card = random.randint(1,10)
    sets.append(card)
    print(sets)

random_card()
random_card()
random_card()
random_card()'''

class user(object):
    def __init__(self,cash, rewards, name):
        self.cash = cash
        self.rewards = rewards
        self.name = name

player_1 = user(100,0,"Jim")
bet = None
def betting():
    bet = int(input("How much are you betting?"))
    if player_1.cash-bet <0:
        print("You don't have that much to spend. \nHow about you burrow some money?")
        burrow_money()
        betting()
    else:
        blackjack()


def burrow_money():
    print("\nYou currently have "+ str(player_1.cash))
    loan = int(input("How much would you like to burrow?"))
    player_1.cash+=loan

betting()


def end():
    if sum(dealer_cards) < sum(player_cards) and sum(player_cards <= 21):
        balance = bet * 2
        player_1.cash += balance
        print("Player Wins!")
    elif sum(player_cards) < sum(dealer_cards) and sum(dealer_cards) <= 21:
        player_1.cash -= bet
        print("Dealer Wins!")
    elif sum(player_cards) > sum(dealer_cards) and sum(dealer_cards) <= 21:
        player_1.cash -= bet
        print("Dealer Wins!")
    elif sum(player_cards) == sum(dealer_cards) and sum(player_cards) <= 21 and sum(dealer_cards) <= 21:
        print("Draw!")
    elif sum(player_cards) < sum(dealer_cards) and sum(player_cards) <= 21:
        balance = bet * 2
        player_1.cash += balance
        print("Player Wins")
    else:
        print("Something went wrong")