import hunger, mine, random, practical

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

def getApple(backpack):
    backpack.append("apple")
    print("you got an apple")

def getLog(backpack):
    backpack.append("log")
    print("you got a log")
    
    x = random.randint(1,5)
    if x == 3:
        getApple(backpack)

def getStone(backpack):
    check = checkPickaxe("stone", requirements, pickaxe, backpack)

    if check == True:
        backpack.append("stone")
        print("you got stone")
    else:
        print("you need a better pickaxe")

def getWheat(backpack):
    backpack.append("wheat")
    print("you got a piece of wheat")

#get

getting = {
    "stone":mine.mining,
    "log":getLog,
    "iron":mine.mining,
    "diamond":mine.mining,
    "wheat":getWheat,
    "meat":hunger.hunting,
    "coal":mine.mining
}

def get(materials, backpack):
    aim = input("what do you want to get? [press o for options] ")
    print("")
    
    if aim == "o":
        practical.options(materials)
    elif aim not in materials:
        print("cannot be collected")
    else:
        getting[aim](backpack)
        hunger.loseHunger()