backpack = ["coal"]

beforeAfter = dict({
    ("iron ore", "iron"),
    ("raw meat", "cooked meat")})

def furnace(backpack, item):
    backpack.remove(item)
    backpack.remove("coal")
    backpack.append(beforeAfter[item])

def useFurnace(backpack, item):
    if item in backpack:
        if "coal" in backpack:
            furnace(backpack, item)
        else:
            print("you need coal")
    else:
        print("item not in backpack")

print(backpack)
useFurnace(backpack, "raw meat")
print(backpack)