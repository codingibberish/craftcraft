import random, time, practical, hunger

pickaxe = ["wooden pickaxe", "stone pickaxe", "iron pickaxe", "diamond pickaxe"]

requirements = {
    "log":"axe",
    "stone":"wooden pickaxe",
    "coal":"wooden pickaxe",
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

def mining(backpack):
    print("you head off into the mines..\n")
    time.sleep(1)

    on = True

    while on == True:

        caveChance = random.randint(1,10)

        if caveChance == 10:
            cave(backpack)
        else:
            ores=["iron", "iron", "iron", "diamond", "stone", "stone", "stone", "stone", "coal", "coal", "coal"]
            found = random.choice(ores)

            print(f"you mine until you find {found}\n")
            time.sleep(1)
            print(f"do you want to mine the {found}?")
            human = input()

            if human == "yes" or human == "y":
                check = checkPickaxe(found, requirements, pickaxe, backpack)

                if check == True:
                    backpack.append(found)
                    print(f"\nyou got {found}")
                    hunger.loseHunger()
                else:
                    print("you need a better pickaxe\n")
            else:
                pass
            


        ask = 0

        while ask != 1:
            ask = input("\nmenu: continue [c]  quit [q]  backpack [b] see stats [s]  eat [e]")
            print("")
            if ask == "c":
                ask = 1
            elif ask =="q":
                ask = 1
                on = False
            elif ask == "b":
                practical.seeBackpack(backpack)
                print("")
            elif ask =="s":
                hunger.showStats()
                print("")
            elif ask == "e":
                hunger.eat(backpack)
                print("")

def cave(backpack):

    print("you stumble across a cave...")
    time.sleep(1)

    ores = ["iron", "iron", "diamond", "stone", "stone", "coal", "coal"]

    amount = random.randint(3,6)
    inCave = []

    for i in range(amount):
        inCave.append(random.choice(ores))
    
    print("\nthere is [", end=" ")
    for i in inCave:
        print(i, end=" ")
    print("] in the cave")

    human = input("\nmine it all? [y/n]")

    if human.lower() == "y":
        for i in inCave:
            if checkPickaxe(i, requirements, pickaxe, backpack) == True:
                backpack.append(i)
        print("\nyou leave the cave with a full backpack")
    else:
        print("\nyou leave the cave empty handed")
