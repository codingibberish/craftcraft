#craftcraft || 27/11/21

"""
to do:

    1. learn classes
    2. instructions
    3. farming
    4. build a house -> get a furnace -> smelt items -> add a farm -> grow wheat

"""

import practical, hunger, craft, get

#declare variables
backpack = ["axe"]
recipes = dict([
    ("plank", ["log"]),
    ("stick", ["plank"]),
    ("wooden pickaxe", ["plank", "plank", "plank", "stick", "stick"]),
    ("stone pickaxe", ["stone", "stone", "stone", "stick", "stick"]),
    ("iron pickaxe", ["iron", "iron", "iron", "stick", "stick"]),
    ("diamond pickaxe", ["diamond", "diamond", "diamond", "stick", "stick"]),
    ("bread", ["wheat", "wheat", "wheat"]),
    ("furnace", ["stone", "stone", "stone", "stone", "stone", "stone", "stone", "stone"])
])
items = ["log", "plank", "stick", "wooden pickaxe", "stone", "stone pickaxe", "iron ore", "iron", "iron pickaxe", "diamond", "wheat", "bread", "apple", "meat", "cooked meat", "diamond pickaxe", "furnace", "coal"]
materials = ["log", "stone", "iron", "diamond", "wheat", "meat", "coal"]

#run game

def game():
    play = True

    while play == True:
        print("")
        human = input("menu: craft [c] | get materials [g] | see all controls [i]   >>>  ")
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