def cheats(backpack):
    add = input("add: ")
    backpack.append(add)

def findRecipe(recipes):
    human = input("what recipe would you like to see? ")
    if human in recipes:
        print(human, ": ", end="")
        for i in recipes[human]:
            print("[",i,"]", " ", end="")
    elif human == "all":
        for x, y in recipes.items():
            print("")
            print(x + " : ", y )
            print("")
    else:
        print("not a valid recipe")

def controls():
    print("press [c] to craft")
    print("press [g] to get materials")
    print("press [e] to eat")
    print("press [t] to trash an item")
    print("press [b] to see backpack")
    print("press [r] to recipes")
    print("press [s] to show stats")
    print("press [q] to quit")
    print("")

def options(materials):
    print("")
    print("[  ", end="")
    for item in materials:
        print(item, end=" ")
    print(" ]")

def trash(backpack):
    human = input("what item would you like to trash? ")
    if human == "axe":
        print("you can't throw away your axe")
    elif human in backpack:
        backpack.remove(human)
    else:
        print("you don't have a " + human + " to trash")

def seeBackpack(backpack):
    if not backpack:
        print("backpack: empty")
    else:
        print("backpack: ", end=" ")

        temp = []
        for item in backpack:
            if item not in temp:
                x = backpack.count(item)
                temp.append(item)
                if x == 1:
                    print(item, end="  ")
                else:
                    print(item, "[" + str(x) + "]", end="  ")
        print()

#testing