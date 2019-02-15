# Currently written for only one class
# from datetime import datetime  # maybe to create a save feature
from datetime import time
from os import sys
import os

no_list = ["no", "n", "N", "No"]
yes_list = ["yes", "y", "Y", "Yes"]
name = ""
name_var = True
while name_var == True:
    try:
        name = input("Enter character name.")
        name_var = False
    except IndexError:
      print ("test")
first_letter = name[0]
rest_of_name = name[1:len(name)]
lower_rest_of_name = rest_of_name.lower()
Cap_first_letter = first_letter.upper()
name = Cap_first_letter + lower_rest_of_name
print("Hello " + name + "! Welcome to this simulation.")
# def Class_change(object):

Classes = ['Mage']
User_class = ""
Skills = ['Overall_level', "strength", "intelligence", "agility"]

# def stats(Class):
# print Class()
# print


class Class(object):
    def __init__(self, name, Overall_level, strength, intelligence, agility):
        self.name = name
        self.Overall_level = Overall_level
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility

    inventory = {
        'gold': 150,
        'pouch': [],
        'backpack': []

    }


class Mage(Class):
    def __init__(self, name, Overall_level, strength, intelligence, agility):
        self.name = name
        self.Overall_level = Overall_level
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility

    inventory = {
        'gold': 300,
        'pouch': ['Ring of Frost', 'Staff of Wisdom'],
        'backpack': []
    }


# print("Chosen class %s" %())
print('Select a class from below')
print(str(Classes), sep=", ")
Pick_class = input("Class:")
Pick_class = Pick_class
if Pick_class is None:
    print("Please select another class.")
if Pick_class != "":
    first_letter_C = Pick_class[0]
    rest_of_class_name = Pick_class[1:len(Pick_class)]
    Cap_first_letter_C = first_letter_C.upper()
    Title = Cap_first_letter_C + rest_of_class_name
if Title == "M":  # error occurs if Pick_class doesn't get an input
    Title = "Mage"
elif Title == "Blank":  # placeholder for now
    Title = "Blank"
if Title == "M" or "Mage":
    print("A young " + Title + " I see its been a long time since I\'ve met one of those.")


# Mage_stats = Mage(name, 1, 2, 8, 3) for the future when I get good
Mage_stats = {"Overall_level": 1, "strength": 2, "intelligence": 8, "agility": 3}
Mage_inventory = {
    'gold': 300,
    'pouch': ['Ring of Frost'],
    'backpack': ['Staff of Wisdom']
}


# print(Mage_stats.agility) will print the value
# print("\nAvailable skills are " + str(Skills))  # coppy paste at the end of all outcomes.
# print("To check skill level enter: \n 'Class'_stats" +
# " with the first letter of your class capitalized \n ")
# find a way to make sure the first letter will always be a capital
print("Available items are " + str(Mage_inventory))  # copy paste at the end of all outcomes.
# print("To check items enter: \n 'Class'_inventory" +
# " with the first letter of your class capitalized \n ")

# need to find a way to put a input at the end of all actions

print("\nNow that you know the basics tis' time for an adventure!")

clear()

print("You are walking down a dirt path when you come across a hooded figure in the distance, Hello there! he yells. \nYou decide to continue towards him, How may I help you? Jimmy\'s the name, Potions are my game.\nWell you do have anything an adventurer could use?\nOf course I do, I\'ve got anything you could ever imagine!\nWhat about a fire potion? \n*Searches bag*\nOutta luck kid, just sold my last one.")
print("I do have this potion that I\'ve been working on, haven\'t got a name for it but I do know it has gotten me out of many pickles.\nWhy don\'t you take it for a measly 100 gold?")
sit1 = ""
sit1 = input("Do you take the potion or not?(y or n)")
# needed this for some reason, try changin alphabet value to numeric values might work better
first_letter_sit1 = sit1[0]
Cap_first_letter_sit1 = first_letter_sit1.upper()
sit1 = Cap_first_letter_sit1

if sit1 in no_list:
    print("")
    print("No thanks sir")
elif sit1 in yes_list:
    Mage_stats["Overall_level"] = 1
    Mage_inventory['backpack'].append("potion")
    Mage_inventory["gold"] -= 100
    print(" ")
    print("Thank you sir!")
    print("You now have " + str(Mage_inventory))
print(" \n ")


# Game over path
# elif sit1 == "2":
# print("Game Over")
# quit()
# time.sleep(.5)
# os.execv(__file__, sys.argv)
print("You continue to travel down the forest path. As you begin to reach the end of it, you become blinded by a light as you shield your eyes, it disappears only for you to see a whole new mythical world. Filled with creatures running about freely, just as you are about to begin exploring you start to get a feeling that you are being watched. You look around but see no one behind you.")
print("Walking out of the forest you gaze out to see nothing but what seems to be an empty field. You begin walking through the tall grass when all of a sudden you get another feeling that you are being watched, you spin around but this time you find someone is actually following you.")
print("*BAM* All of a sudden you feel numb and drop to the ground.")
print("The ground shakes as you wake up, in front of you a rock like creature roars in your face. You scramble backwards as fast as you can, heart racing the beast begins to charge at you.")
print(" ")
sit2 = ""
print(Mage_stats)
print("")
sit2 = input(
    "What do you do? Try to use a spell (int), you wind up and attempt to punch the beast (str) or dodge it (agt)?")
print(Mage_stats)
if sit2 == "int":
    sit2 = 1
elif sit2 == "agt":
    sit2 = 2
elif sit2 == "str":
    sit2 = 3


if sit2 == 1:
    Mage_stats["Overall_level"] = 2
    print("\nLevel up!")
    print(Mage_stats)
    print("\nYou cast a spell that stops it right where it stands, you decide to approach it. As you keep getting closer it keeps repeating 'Must \nComplete \nQuest'. ")
elif sit2 == 2:
    print("\nYou nearly dodge it but are clipped by a shard sticking out and are spun around but you catch your footing and land softly in a patch of grass. While the beast trips over a rock and takes a hard fall onto it's head, becoming dazed.")
elif sit2 == 3:
    print("\nIt catches your hand and tosses you over its shoulder and you take a hard landing in the field")
else:
    print("Error")

print("\n")
print("After interrogating the beast for a few minutes, you decide you let it go on the condition that it would bring you back to who sent it.")
print("After much resistance the beast ultimately gives in to your demands, ")
print("To Be Continued")
