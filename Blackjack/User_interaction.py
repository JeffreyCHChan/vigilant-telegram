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
