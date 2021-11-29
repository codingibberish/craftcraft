#craftcraft || 27/11/21

"""
to do:

    1. learn classes
    2. make diamonds harder to get & make mining less shit
    3. instructions
    4. farming
    5. house/chest
    8. add caves to mining


"""

import random
import time
import practical, mine, hunger, craft, get

#declare variables
backpack = ["axe"]
recipes = dict([
    ("plank", ["log"]),
    ("stick", ["plank"]),
    ("wooden pickaxe", ["plank", "plank", "plank", "stick", "stick"]),
    ("stone pickaxe", ["stone", "stone", "stone", "stick", "stick"]),
    ("iron pickaxe", ["iron", "iron", "iron", "stick", "stick"]),
    ("bread", ["wheat", "wheat", "wheat"])
])
items = ["log", "plank", "stick", "wooden pickaxe", "stone", "stone pickaxe", "iron", "iron pickaxe", "diamond", "wheat", "bread", "apple", "meat"]
materials = ["log", "stone", "iron", "diamond", "wheat", "meat"]

#run game

def game():
    play = True

    while play == True:
        print("")
        human = input("menu: craft [c] | get materials [g] | see all controls [i]\n")
        print("")

        if human == "q":
            print("quitting game...")
            play = False
        elif human == "c":
            craft.craft(recipes, backpack)
        elif human == "b":
            practical.seeBackpack(backpack)
        elif human == "g":
            get.get(materials, backpack)
        elif human == "r":
            practical.findRecipe(recipes)
        elif human == "t":
            practical.trash(backpack)
        elif human == "i":
            practical.controls()
        elif human == "z":
            practical.cheats(backpack)
        elif human == "e":
            hunger.eat(backpack)
        elif human =="s":
            hunger.showStats()

game()