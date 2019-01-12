import random
no_list = ["no", "n", "N", "No"]
yes_list = ["yes", "y", "Y", "Yes"]
anonymous = ["-A", "-a"]
hit = ['Hit', 'hit', "H", "h"]
stay = ['Stay', 'stay', "S", "s"]
try:
    name = input("What's your name.")
    first_letter = name[0]
    rest_of_name = name[1:len(name)]
    lower_rest_of_name = rest_of_name.lower()
    Cap_first_letter = first_letter.upper()
    name = Cap_first_letter + lower_rest_of_name
    print(name)
except IndexError:
    print ("No name was entered, if you would like to play anonymously enter -A or -a")
    name = input("What is your name?")
    if name in anonymous:
        print("Welcome Stranger!")


#class user(object):

   # inventory = {
        #'cash': 300,
      #  'rewards': []}
def blackjack():
    player_sum = 0
    dealer_sum = 0
    def pCal():
        p = sum(player_cards)
        print(p)
        return (int(p))
    def hand_value():
        player_sum = sum(player_cards)
        print(player_sum)
    under_limit=21
    #used_card = []
    player_cards = []
    dealer_cards = []
    card = random.randint(1, 10)
    First_card = random.randint(1, 10)
    Second_card = random.randint(1, 10) #currently to 10
    def First_Card_flip():

        print("\nLet's get started " + str(First_card) + ' and '+str(Second_card))
        player_cards.append(First_card)
        player_cards.append(Second_card)
        #return used_card.append(First_card,Second_card)
        #return maybe for when counting cards to append to used_cards
    First_Card_flip()
    def Hit_or_miss():
        cycle = True
        while cycle == True:
            hit = ['Hit', 'hit', "H", "h"]
            stay = ['Stay', 'stay', "S", "s"]
            if First_card  + Second_card <= under_limit:
                next_move=input("Hit or Stay?")
                if next_move in hit:
                    third_card = random.randint(1, 10)
                    print (str(player_cards[0]) + "," + str(player_cards[1]) +','+ str(third_card))
                    player_cards.append(third_card)
                    pCal()
                elif next_move in stay:
                    print (player_cards)
                    return(hand_value())
                    return cycle == False

            if player_cards[0] + player_cards[1] + player_cards[2] <= 21:
                next_move2 = input("Hit or Stay?")
                if next_move2 in hit:
                    fourth_card = random.randint(1, 10)
                    print(str(player_cards[0]) + "," + str(player_cards[1]) + ',' + str(player_cards[2])+ ','+
                          str(fourth_card))
                    player_cards.append(fourth_card)
                elif next_move2 in stay:
                    print(player_cards)
                    return (hand_value())
                    return cycle == False
            elif player_cards[0] + player_cards[1] + player_cards[2] > 21:
                print(hand_value())
                print("Over 21. You Lose!")
                return cycle == False

            if player_cards[0] + player_cards[1] + player_cards[2] + player_cards[3] <= 21:
                next_move3 = input("Hit or Stay?")
                if next_move3 in hit:
                    five_card = random.randint(1, 10)
                    print(str(player_cards[0]) + "," + str(player_cards[1]) + ',' + str(player_cards[2]) +
                          ',' + str(player_cards[3]) + ',' + str(five_card))
                    player_cards.append(five_card)
                    if player_cards[0] + player_cards[1] + player_cards[2] + player_cards[3] + player_cards[4]> 21:
                        print("Over 21. You Lose!")
                        break

                elif next_move3 in stay:
                    print(player_cards)
                    return hand_value()
                    return cycle == False
            elif player_cards[0] + player_cards[1] + player_cards[2] + player_cards[3] > 21:
                print(hand_value())
                print("Over 21. You Lose!")
                return cycle == False

            if player_cards[0] + player_cards[1] + player_cards[2] + player_cards[3] + player_cards[4] <= 21:
                next_move4 = input("Hit or Stay?")
                if next_move4 in hit:
                    six_card = random.randint(1, 10)
                    print(str(player_cards[0]) + "," + str(player_cards[1]) + ',' + str(player_cards[2]) + ','
                          + str(player_cards[3]) + ',' + str(player_cards[4]) + ',' +str(six_card))
                    player_cards.append(six_card)
                    if player_cards[0] + player_cards[1] + player_cards[2] + player_cards[3] + player_cards[4] + \
                            player_cards[5] > 21:
                        print("Over 21! You lose!")
                        break
                elif next_move4 in stay:
                    print(player_cards)
                    print(hand_value())
                    return cycle == False
            elif player_cards[0] + player_cards[1] + player_cards[2] + player_cards[3] > 21:
                print(hand_value())
                print("Over 21. You Lose!")
                return cycle == False

    def Dealer():

        dealer_card1 = random.randint(1, 10)
        dealer_card2 = random.randint(1, 10)
        dealer_cards.append(dealer_card1)
        dealer_cards.append(dealer_card2)
        D_under_limit = random.randint(17, 21)
        def dealer_flip():
            dx=0
            def D_hand_value():
                dealer_sum = sum(dealer_cards)
                dx = dealer_sum
                return dx
                print(dealer_sum)
                print(dx)
            cycle = True
            #while cycle == True:
            hit = ['Hit', 'hit', "H", "h"]
            stay = ['Stay', 'stay', "S", "s"]
            print("\nDealer\'s cards: " + str(dealer_cards[0]) + "," + str(dealer_cards[1]))
            if dealer_card1 + dealer_card2 < D_under_limit:
                D_third_card = random.randint(1, 10)
                dealer_cards.append(D_third_card)
            else:

                return (D_hand_value())
                return cycle == False

            if dealer_cards[0] + dealer_cards[1] + dealer_cards[2] <= D_under_limit:
                D_four_card = random.randint(1, 10)
                dealer_cards.append(D_four_card)
            else:

                return(D_hand_value())
                return cycle == False

            if dealer_cards[0] + dealer_cards[1] + dealer_cards[2] + dealer_cards[3] <= D_under_limit:
                D_five_card = random.randint(1, 10)

                dealer_cards.append(D_five_card)
            else:

                return (D_hand_value())
                return cycle == False

            if dealer_cards[0] + dealer_cards[1] + dealer_cards[2] + dealer_cards[3] + dealer_cards[4]<= D_under_limit:
                D_six_card = random.randint(1, 10)
                dealer_cards.append(D_six_card)
            else:
                print(dealer_cards)
                return (D_hand_value())
                return cycle == False


        dealer_flip()

    def replay():
        replay = input("Would you like to play again?")
        if replay in yes_list:
            blackjack()
        else:
            print("Too bad :(")
    def end():
        if dealer_sum < player_sum:
            print("Player Wins!")
        elif player_sum < dealer_sum :
            print("Player Wins!")
        elif player_sum < dealer_sum:
            print("Dealer Wins!")
        elif player_sum > dealer_sum :
            print("Dealer Wins!")
        elif player_sum == dealer_sum:
            print("Draw!")
        else:
            print("Something went wrong")
    Hit_or_miss()
    Dealer()
    end()
    replay()
blackjack()
