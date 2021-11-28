from stats import loseHealth, printHealthBar, gainHealth, healthBar


hungerBar = ["🍖", "🍖", "🍖", "🍖", "🍖", "🍖", "🍖", "🍖", "🍖", "🍖"]

def hunger():
    return len(hungerBar)

def loseHunger():
    if len(hungerBar) > 0:
        hungerBar.remove("🍖")
        return len(hungerBar)
    else:
        print("you lost a health point")
        loseHealth()
        printHealthBar()

def gainHunger(fp):
    for i in range(fp):
        if len(hungerBar) < 10:
            hungerBar.append("🍖")

def printHungerBar():
    print("")
    hungry = 10 - len(hungerBar)
    newList = list(hungerBar)

    for x in range(hungry):
        newList.append("🦴")

    for y in newList:
        print(y, " ", end="")
    print("\n")

#food

food = dict([
    ("bread", 4),
    ("apple", 1)
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
    human = input("what do you want to eat? ")
    
    if human in food:
        if human in backpack:
            eatFood(human, food[human], backpack)
        else:
            print("\nitem not in backpack")
    else:
        print("item not available for eating")
