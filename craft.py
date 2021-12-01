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

def makeDiamondPickaxe(backpack):
    for i in range(3):
        backpack.remove("diamond")
    for i in range(2):
        backpack.remove("stick")
    backpack.append("diamond pickaxe")

def makeBread(backpack):
    for i in range(3):
        backpack.remove("wheat")
    backpack.append("bread")

def makeFurnace(backpack):
    for i in range(8):
        backpack.remove("stone")
    backpack.append("furnace")

#craft

crafting = {
    "plank":makePlank,
    "stick":makeStick,
    "wooden pickaxe":makeWoodenPickaxe,
    "stone pickaxe":makeStonePickaxe,
    "iron pickaxe":makeIronPickaxe,
    "diamond pickaxe":makeDiamondPickaxe,
    "bread":makeBread,
    "furnace":makeFurnace
}

def inBackpack(aim, recipes, backpack):
    for item in recipes[aim]:
        if item not in backpack:
            return False
        else:
            x = recipes[aim].count(item)
            y = backpack.count(item)
            if x > y:
                return False

def craft(recipes, backpack):
    aim = input("what do you want to craft? ")

    if aim not in recipes:
        print("\ncannot be crafted")
    else:
        if inBackpack(aim, recipes, backpack) == False:
            print("\nitems not in backpack")
        else:
            crafting[aim](backpack)
            print("\ncrafting " + aim)