import random
import numpy as np
from UserInteraction import *
from tkinter import *
import os


no_list = ["no", "n", "N", "No"]
yes_list = ["yes", "y", "Y", "Yes"]
#player = {'Money' : 5, "Wins":0, 'Losses':0}


Player = User(500, 0, 0, "Jim")

def blackjack():
    def hitClick():
        P_random_card()
        sum(player_cards)
        if sum(player_cards)>21:
            end()
        gui()

    def stayClick():
        sum(player_cards)
        Dealer()
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

    def Dealer():
        cycle = True
        while cycle == True:
            if sum(dealer_cards) < 17:
                D_random_card()
            else:
                cycle == False
                end()


    root = Tk()
    root.geometry("500x200")





    def replay():
        def exitReplay():
            print("Too Bad !")
            quit()

        def restart():
            replayTk.destroy()
            blackjack()
        replayTk = Tk()
        replayTk.geometry("200x200+100+300")
        replayLabel = Label(replayTk, text = "Replay Again")
        replayYes = Button(replayTk, text = "Yes", command=restart)
        replayNo = Button(replayTk, text="No", command=exitReplay)
        replayLabel.pack()
        replayYes.pack()
        replayNo.pack()
        replayTk.mainloop()
        replayTk.quit()
        #blackjack()



    def end():
        if sum(dealer_cards) < sum(player_cards) and sum(player_cards) <= 21:
            sit = Tk()
            sit.geometry("300x200+300+300")

            dealerLabel = Label(sit, text='Dealer\'s Cards')
            dealCards = Entry(sit)
            for x in dealer_cards:
                dealCards.insert(INSERT, str(x) + "    ")
            playerLabel = Label(sit, text="Player\'s Cards")
            playerCards = Entry(sit)
            for x in player_cards:
                playerCards.insert(INSERT, str(x) + "    ")
            dealerLabel.grid(row=0, column=0)
            dealCards.grid(row=1, column=0)
            playerLabel.grid(row=3, column=3)
            playerCards.grid(row=4, column=3)

            WinText=Label(sit, text="Player wins!")

            WinText.grid(row=4,column=0)
            root.destroy()
            replay()
            sit.mainloop()
            sit.destroy()


        elif sum(player_cards) < sum(dealer_cards) and sum(dealer_cards)<=21:

            sit = Tk()
            sit.geometry("300x200+300+300")

            dealerLabel = Label(sit, text='Dealer\'s Cards')
            dealCards = Entry(sit)
            for x in dealer_cards:
                dealCards.insert(INSERT, str(x) + "    ")

            playerLabel = Label(sit, text="Player\'s Cards")
            playerCards = Entry(sit)
            for x in player_cards:
                playerCards.insert(INSERT, str(x) + "    ")
            dealerLabel.grid(row=0, column=0)
            dealCards.grid(row=1, column=0)
            playerLabel.grid(row=3, column=3)
            playerCards.grid(row=4, column=3)

            WinText=Label(sit,text="Dealer wins")
            WinText.grid(row=4,column=0)
            root.destroy()
            replay()
            sit.mainloop()
            sit.destroy()

        elif sum(player_cards) > sum(dealer_cards) and sum(dealer_cards) <= 21 :
            sit = Tk()
            sit.geometry("300x200+300+300")

            dealerLabel = Label(sit, text='Dealer\'s Cards')
            dealCards = Entry(sit)
            for x in dealer_cards:
                dealCards.insert(INSERT, str(x) + "    ")
            playerLabel = Label(sit, text="Player\'s Cards")
            playerCards = Entry(sit)
            for x in player_cards:
                playerCards.insert(INSERT, str(x) + "    ")
            dealerLabel.grid(row=0, column=0)
            dealCards.grid(row=1, column=0)
            playerLabel.grid(row=3, column=3)
            playerCards.grid(row=4, column=3)

            WinText=Label(sit,text="Dealer wins")
            WinText.grid(row=4,column=0)
            root.destroy()
            replay()
            sit.mainloop()
            sit.destroy()
        elif sum(player_cards) == sum(dealer_cards) and sum(player_cards)<=21 and sum(dealer_cards)<=21:
            sit = Tk()
            sit.geometry("300x200+300+300")

            dealerLabel = Label(sit, text='Dealer\'s Cards')
            dealCards = Entry(sit)
            for x in dealer_cards:
                dealCards.insert(INSERT, str(x) + "    ")
            playerLabel = Label(sit, text="Player\'s Cards")
            playerCards = Entry(sit)
            for x in player_cards:
                playerCards.insert(INSERT, str(x) + "    ")
            dealerLabel.grid(row=0, column=0)
            dealCards.grid(row=1, column=0)
            playerLabel.grid(row=3, column=3)
            playerCards.grid(row=4, column=3)

            WinText=Label(sit,text="Draw")
            WinText.grid(row=4,column=0)
            root.destroy()
            replay()
            sit.mainloop()
            sit.destroy()
        elif sum(player_cards) < sum(dealer_cards) and sum(player_cards) <=21:
            sit = Tk()
            sit.geometry("300x200+300+300")

            dealerLabel = Label(sit, text='Dealer\'s Cards')
            dealCards = Entry(sit)
            for x in dealer_cards:
                dealCards.insert(INSERT, str(x) + "    ")
            playerLabel = Label(sit, text="Player\'s Cards")
            playerCards = Entry(sit)
            for x in player_cards:
                playerCards.insert(INSERT, str(x) + "    ")
            dealerLabel.grid(row=0, column=0)
            dealCards.grid(row=1, column=0)
            playerLabel.grid(row=3, column=3)
            playerCards.grid(row=4, column=3)

            WinText=Label(sit,text="Player wins!")
            WinText.grid(row=4,column=0)
            root.destroy()
            replay()
            sit.mainloop()
            sit.destroy()
        else:
            print("Something went wrong")


    def gui():
        dealerLabel = Label(root, text='Dealer\'s Cards')
        dealCards = Entry(root)
        dealCards.insert(ANCHOR, str(dealer_cards[0]))
        playerLabel = Label(root, text="Player\'s Cards")
        playerCards = Entry(root)
        for x in player_cards:
            playerCards.insert(INSERT, str(x)+"    ")
        hitButton = Button(root, text="Hit", padx=20, command=hitClick)
        stayButton = Button(root, text="Stay", padx=20, command=stayClick)
        dealerLabel.grid(row=0, column=0)
        dealCards.grid(row=1, column=0)
        playerLabel.grid(row=3, column=3)
        playerCards.grid(row=4, column=3)
        hitButton.grid(row=4, column=1)
        stayButton.grid(row=4, column=2)
        root.mainloop()

    initial()
    gui()
