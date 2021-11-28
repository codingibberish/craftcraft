#craftcraft || 27/11/21

"""
to do:

    1. add food and hunger
    2. see stats (hunger, health)
    2. learn classes
    2. make backpack output nicer
    3. make diamonds harder to get
    6. instructions

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
items = ["log", "plank", "stick", "wooden pickaxe", "stone", "stone pickaxe", "iron", "iron pickaxe", "diamond", "wheat", "bread"]
materials = ["log", "stone", "iron", "diamond", "wheat", "bread"]

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

game()