import random
import time

def mining(material, backpack):

    print("you head off into the mines...")
    time.sleep(1)

    on = True
    while on == True:
        #generate direction
        direction = random.choice(["right", "left", "center"])
        humanDirection = "one"
        #get human input
        while direction != humanDirection:
            humanDirection = input("left, right or center? ")
            #if human input doesn't match, loops back
            if humanDirection != direction:
                print("there is no " + material + " in this direction...")
        #if human input does match, print this
        print("you're going in the right direction")

        #check for diamonds against random num gen
        location = random.randint(1,5)
        humanLocation = 0
        #get human input
        while location != humanLocation:
            humanLocation = int(input("how far do you want to mine? [you can mine up to 5 blocks] "))
            if location != humanLocation:
                print("keep mining...")
        #break loop if guessed right
        print("you found " + material + "!")
        backpack.append(material)
        on = False