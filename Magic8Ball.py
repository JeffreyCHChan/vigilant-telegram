import random
import os
no_list = ["no", "n", "N", "No"]
yes_list = ["yes", "y", "Y", "Yes"]
anonymous = ["-A", "-a"]
def Magic8Ball():
    question = input("What is your question?")
    print("Magic 8 Ball Magic 8 Ball" + ", " + question + "? ")
    num =random.randint(1, 8)
    if num == 1:
        print('Yes')
    elif num == 2:
        print("Future is unclear")
    elif num == 3 or num == 4:
        print("It is certain.")
    elif num == 5 or num == 6:
        print("My sources say no.")
    elif num == 7 or num == 8:
        print("Cannot predict now.")
    cont = input("\nWould you like to ask another question? Y or N")
    if cont in yes_list:
        Magic8Ball()
    elif cont in no_list:
        exit()

Magic8Ball()