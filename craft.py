def makePlank(backpack):
    backpack.remove("log")
    for i in range(4):
        backpack.append("plank")

def makeStick(backpack):
    backpack.remove("plank")
    for i in range(4):
        backpack.append("stick")

def makeWoodenPickaxe(backpack):
    for i in range(3):
        backpack.remove("plank")
    for i in range(2):
        backpack.remove("stick")
    backpack.append("wooden pickaxe")

def makeStonePickaxe(backpack):
    for i in range(3):
        backpack.remove("stone")
    for i in range(2):
        backpack.remove("stick")
    backpack.append("stone pickaxe")

def makeIronPickaxe(backpack):
    for i in range(3):
        backpack.remove("iron")
    for i in range(2):
        backpack.remove("stick")
    backpack.append("iron pickaxe")

def makeBread(backpack):
    for i in range(3):
        backpack.remove("wheat")
    backpack.append("bread")

#craft

crafting = {
    "plank":makePlank,
    "stick":makeStick,
    "wooden pickaxe":makeWoodenPickaxe,
    "stone pickaxe":makeStonePickaxe,
    "iron pickaxe":makeIronPickaxe,
    "bread":makeBread
}

def inBackpack(aim, recipes, backpack):
    for item in recipes[aim]:
        if item not in backpack:
            return False
        else:
            return True

def craft(recipes, backpack):
    aim = input("what do you want to craft? ")

    if aim not in recipes:
        print("cannot be crafted")
    else:
        if inBackpack(aim, recipes, backpack) == False:
            print("items not in backpack")
        else:
            crafting[aim](backpack)
            print("crafting " + aim)