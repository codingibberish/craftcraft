import random

hungerBar = ["ð", "ð", "ð", "ð", "ð", "ð", "ð", "ð", "ð", "ð"]
healthBar = ["ð", "ð", "ð", "ð", "ð", "ð", "ð", "ð", "ð", "ð"]

#health functions

def health():
    return len(healthBar)

def loseHealth():
    if len(healthBar) > 0:
        healthBar.remove("ð")
        return len(healthBar)
    else:
        print("you died")
        quit()

def gainHealth():
    healthBar.append("ð")

def printHealthBar():
    print("")
    hurt = 10 - len(healthBar)
    newList = list(healthBar)

    for x in range(hurt):
        newList.append("ðĪ")
        
    for y in newList:
        print(y, " ", end="")
    print("\n")


def showStats():
    printHungerBar()
    printHealthBar()

#hunger functions

def hunger():
    return len(hungerBar)

def loseHunger():
    if len(hungerBar) > 0:
        hungerBar.remove("ð")
        return len(hungerBar)
    else:
        print("you lost a health point")
        loseHealth()
        printHealthBar()

def gainHunger(fp):
    for i in range(fp):
        if len(hungerBar) < 10:
            hungerBar.append("ð")

def printHungerBar():
    print("")
    hungry = 10 - len(hungerBar)
    newList = list(hungerBar)

    for x in range(hungry):
        newList.append("ðĶī")

    for y in newList:
        print(y, " ", end="")
    print("\n")

#food and eating

food = dict([
    ("bread", 5),
    ("apple", 2),
    ("cooked meat", 7)
])

def eatFood(item, fp, backpack):
    if len(hungerBar) >= 10:
        print("you're too full to eat")
    elif len(healthBar) < 10:
        print("you regain health and hunger")
        gainHunger(fp)
        while len(healthBar) < 10:
            gainHealth()
    else:
        print("you eat the", item, "and regain", fp, "hunger")
        gainHunger(fp)
        printHungerBar()
        backpack.remove(item)

def eat(backpack):
    printHungerBar()
    human = input("\nwhat do you want to eat? ")
    
    if human in food:
        if human in backpack:
            eatFood(human, food[human], backpack)
        else:
            print("\nitem not in backpack")
    else:
        print("\nitem not available for eating")

#hunting

trees = ["ðģ", "ðģ", "ðģ"]
animals = dict([
    ("cow", "ð"),
    ("pig", "ð"),
    ("sheep", "ð"),
    ("goat", "ð")
])

def hunting(backpack):
    animal = random.choice(["cow", "pig", "goat", "sheep"])
    location = random.randint(1,3)
    
    print("")
    for i in range(len(trees)):
        print("ðģ", end="  ")
    print("")

    human = int(input(f"\nwhich tree is the {animal} hiding behind? "))

    if human >= 1 and human <= 3:
        if human == location:

            for i in range(len(trees)):
                if i == (location-1):
                    print(animals[animal], end="  ")
                else:
                    print("ðģ", end="  ")

            print(f"\nyou find and kill the {animal}")
            backpack.append("meat")
            print("\nmeat has been added to backpack")
        else:
            print(f"\nwrong tree. the {animal} hears you and runs away.")