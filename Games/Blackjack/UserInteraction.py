'''class user(object):
    def __init__(self,cash, rewards, name):
        self.cash = cash
        self.rewards = rewards
        self.name = name
'''


bet = None
def betting():
    bet = int(input("How much are you betting?"))
    if player_1.cash-bet <0:
        print("You don't have that much to spend. \nHow about you burrow some money?")
        burrow_money()
        betting()
    else:
        blackjack()

class User(object):
    def __init__(self, Money, Wins, Losses, name):
        self.Money = Money
        self.Wins = Wins
        self.Losses = Losses
        self.name = name
    def stats(self,Money,Wins,Losses):
        Money
        Wins
        Losses
def burrow_money():
    print("\nYou currently have "+ str(player_1.cash))
    loan = int(input("How much would you like to burrow?"))
    player_1.cash+=loan

#betting()
