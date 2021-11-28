hungerBar = ["%", "%", "%", "%", "%", "%", "%", "%", "%", "%"]

def hunger():
    return len(hungerBar)

def loseHunger():
    if len(hungerBar) > 0:
        hungerBar.remove("%")
        return len(hungerBar)
    else:
        print("n/a for now")

def gainHunger(fp):
    for i in range(fp):
        hungerBar.append("%")

def printHungerBar():
    for i in hungerBar:
        print(i, " ", end="")
    print("\n")

#food

food = dict([
    ("bread", 2)
])

def eatFood(item, fp):
    if len(hungerBar) >= 10:
        print("you're too full to eat")
    else:
        print("you eat the", item, "and regain", fp, "hunger")
        gainHunger(fp)
        printHungerBar()

def eat(backpack):
    printHungerBar()
    human = input("what do you want to eat? ")
    
    if human in food:
        if human in backpack:
            eatFood(human, food[human])
        else:
            print("item not in backpack")
    else:
        print("item not available for eating")

backpack = ["bread"]

loseHunger()
loseHunger()
eat(backpack)