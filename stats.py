import hunger

healthBar = ["💚", "💚", "💚", "💚", "💚", "💚", "💚", "💚", "💚", "💚"]

def health():
    return len(healthBar)

def loseHealth():
    if len(healthBar) > 0:
        healthBar.remove("💚")
        return len(healthBar)
    else:
        print("you died")
        quit()

def gainHealth():
    healthBar.append("💚")

def printHealthBar():
    print("")
    hurt = 10 - len(healthBar)
    newList = list(healthBar)

    for x in range(hurt):
        newList.append("🖤")
        
    for y in newList:
        print(y, " ", end="")
    print("\n")


def showStats():
    hunger.printHungerBar()
    printHealthBar()