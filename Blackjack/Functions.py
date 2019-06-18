import random
import numpy as np


no_list = ["no", "n", "N", "No"]
yes_list = ["yes", "y", "Y", "Yes"]
player = {'Money' : 5, "Wins":0, 'Losses':0}
def blackjack():

    #used_card = []
    player_cards = []
    dealer_cards = []
    def D_Usable_Ace():
        for i in dealer_cards:
            if i== 1 and sum(dealer_cards) <=21:
                dealer_cards.pop()
                dealer_cards.append(11)

    def Usable_Ace():
        for i in player_cards:
            if i== 1 and sum(player_cards) <=21:
                player_cards.pop()
                player_cards.append(11)
    def P_random_card():
        card = random.randint(1,10)
        player_cards.append(card)
    def D_random_card():
        card = random.randint(1, 10)
        dealer_cards.append(card)

    def initial():
        P_random_card()
        P_random_card()
        Usable_Ace()
        D_random_card()
        D_random_card()
        D_Usable_Ace()
        print("\nLet's get started, your cards are " + str(player_cards) +"\n"+str(sum(player_cards)) +"\nDealer cards are " + str(dealer_cards[0]))


        #return used_card.append(First_card,Second_card)
        #return maybe for when counting cards to append to used_cards
    def Hit_or_miss():
        cycle = True
        while cycle == True:
            hit = ['Hit', 'hit', "H", "h"]
            stay = ['Stay', 'stay', "S", "s"]
            if np.sum(player_cards) <= 21:
                next_move=input("Hit or Stay?")
                if next_move in hit:
                    P_random_card()
                    print (player_cards)
                    print(sum(player_cards))
                elif next_move in stay:
                    print (player_cards)
                    print(sum(player_cards))
                    return cycle == False

            if np.sum(player_cards) <= 21:
                next_move = input("Hit or Stay?")
                if next_move in hit:
                    P_random_card()
                    print(player_cards)
                elif next_move in stay:
                    print(player_cards)
                    print(sum(player_cards))
                    return cycle == False
            elif player_cards[0] + player_cards[1] + player_cards[2] > 21:
                print(sum(player_cards))
                print("Over 21. You Lose!")
                return cycle == False

            if sum(player_cards) <= 21:
                next_move = input("Hit or Stay?")
                if next_move in hit:
                    P_random_card()
                    print(player_cards)
                    print(sum(player_cards))
                    if sum(player_cards)> 21:
                        print("Over 21. You Lose!")
                        break

                elif next_move in stay:
                    print(player_cards)
                    print(sum(player_cards))
                    return cycle == False
            elif sum(player_cards) > 21:
                print(sum(player_cards))
                print("Over 21. You Lose!")
                return cycle == False

            if sum(player_cards) <= 21:
                next_move = input("Hit or Stay?")
                if next_move in hit:
                    P_random_card()
                    print(player_cards)
                    print(sum(player_cards))
                    if sum(player_cards) > 21:
                        print("Over 21! You lose!")
                        break
                elif next_move in stay:
                    print(player_cards)
                    print(sum(player_cards))
                    return cycle == False
            elif sum(player_cards) > 21:
                print(player_cards)
                print(sum(player_cards))
                print("Over 21. You Lose!")
                return cycle == False

    def Dealer():

        D_random_card()
        cycle = True
        #while cycle == True:
        if sum(dealer_cards) <= 17:
            D_random_card()
        else:
            print(sum(dealer_cards))
            return cycle == False

        if sum(dealer_cards) <= 17:
            D_random_card()
        else:
            print(sum(dealer_cards))
            return cycle == False

        if sum(dealer_cards) <= 17:
            D_random_card()
        else:
            print(sum(dealer_cards))
            return cycle == False

        if sum(dealer_cards) <= 17:
            D_random_card()
        else:
            print(sum(dealer_cards))
            return cycle == False

    def replay():
        replay = input("Would you like to play again?")
        if replay in yes_list:
            print("\n\n\nCash: %d, Wins: %d, Losses:%d" % (player['Money'], player["Wins"], player["Losses"]))
            blackjack()
        else:
            print("Too bad :(")

    def end():
        if sum(dealer_cards) < sum(player_cards) and sum(player_cards) <= 21:
            player['Money']+= 1
            player["Wins"]+=1
            print("Player Wins!")
        elif sum(player_cards) < sum(dealer_cards) and sum(dealer_cards)<=21:
            player['Money']-= 1
            player["Losses"] += 1
            print("Dealer Wins!")
            print(dealer_cards)
        elif sum(player_cards) > sum(dealer_cards) and sum(dealer_cards) <= 21 :
            player['Money']-= 1
            player["Losses"] += 1
            print("Dealer Wins!")
            print(dealer_cards)
        elif sum(player_cards) == sum(dealer_cards) and sum(player_cards)<=21 and sum(dealer_cards)<=21:
            print("Draw!")
        elif sum(player_cards) < sum(dealer_cards) and sum(player_cards) <=21:
            player['Money']+= 1
            player["Wins"] += 1
            print("Player Wins")
        else:
            print("Something went wrong")
    initial()
    Hit_or_miss()
    Dealer()
    end()
    replay()