import random, time, practical, hunger

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

def mining(backpack):
    print("you head off into the mines..")
    time.sleep(1)

    on = True

    while on == True:
        

        ores=["iron", "iron", "iron", "diamond", "stone", "stone", "stone", "stone"]
        found = random.choice(ores)

        print("you mine until you find", found)
        time.sleep(1)
        print("do you want to mine the", found + "?")
        human = input()

        if human == "yes" or human == "y":
            check = checkPickaxe(found, requirements, pickaxe, backpack)

            if check == True:
                backpack.append(found)
                print("you got", found)
                hunger.loseHunger()
            else:
                print("you need a better pickaxe")
        else:
            pass
            


        ask = 0

        while ask != 1:
            ask = input("menu: continue [c]  quit [q]  backpack [b] see stats [s]  eat [e]")
            if ask == "c":
                ask = 1
            elif ask =="q":
                ask = 1
                on = False
            elif ask == "b":
                practical.seeBackpack(backpack)
            elif ask =="s":
                hunger.showStats()
            elif ask == "e":
                hunger.eat(backpack)