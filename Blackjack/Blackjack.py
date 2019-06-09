from Functions import *

anonymous = ["-A", "-a"]
hit = ['Hit', 'hit', "H", "h"]
stay = ['Stay', 'stay', "S", "s"]
'''try:
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
        print("Welcome Stranger!")'''


#class user(object):

   # inventory = {
        #'cash': 300,
      #  'rewards': []}
blackjack()
