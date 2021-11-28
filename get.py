import mine

pickaxe = ["wooden pickaxe", "stone pickaxe", "iron pickaxe", "diamond pickaxe"]

requirements = {
    "log":"axe",
    "stone":"wooden pickaxe",
    "iron":"stone pickaxe",
    "diamond":"iron pickaxe",
}

def checkPickaxe(item, requirements, pickaxe, backpack):
    #find necessary list placement
    required = requirements[item]
    place = pickaxe.index(required)
    #check if an item above or similar is in backpack

    for i in backpack:
        if i in pickaxe:
            if pickaxe.index(i) >= place:
                return True

#get functions

def getLog(backpack):
    backpack.append("log")
    print("you got a log")

def getStone(backpack):
    check = checkPickaxe("stone", requirements, pickaxe, backpack)

    if check == True:
        backpack.append("stone")
        print("you got stone")
    else:
        print("you need a better pickaxe")

def getIron(backpack):
    check = checkPickaxe("iron", requirements, pickaxe, backpack)

    if check == True:
        mine.mining("iron", backpack)
    else:
        print("you need a better pickaxe")

def getDiamond(backpack):
    check = checkPickaxe("diamond", requirements, pickaxe, backpack)

    if check == True:
        mine.mining("diamond", backpack)
    else:
        print("you need a better pickaxe")

def getWheat(backpack):
    backpack.append("wheat")
    print("you got a piece of wheat")

#get

getting = {
    "stone":getStone,
    "log":getLog,
    "iron":getIron,
    "diamond":getDiamond,
    "wheat":getWheat
}

def get(materials, backpack):
    aim = input("what do you want to get? ")

    if aim not in materials:
        print("cannot be collected")
    else:
        getting[aim](backpack)