#craftcraft || 27/11/21

"""
to do:

    2. learn classes
    4. make diamonds harder to get
    5. make mining less shit
    5. instructions
    7. deal with what happens when there's no hunger left - lose health? - lose health every time u do an action until death
    8. farming

"""

import random
import time
import practical, mine, hunger, craft, get, stats

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
items = ["log", "plank", "stick", "wooden pickaxe", "stone", "stone pickaxe", "iron", "iron pickaxe", "diamond", "wheat", "bread", "apple"]
materials = ["log", "stone", "iron", "diamond", "wheat", "bread", "apple"]

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
            stats.showStats()

game()