# 25/02/2020 pickApath_V1.1.py
# Cory Keastpither

"""
*********************************************
Change Log V1.1
- Added Display Item Screen
- Started Start Screen
-
*********************************************
"""

# imports

import random
import time

# declare Vars
userStats = [100, 50, 25, 100, ["None", "Sword", "Arrow", "Hat"]]
"""
0 = health
1 = stamina
2 = dexterity 
3 = mana
4 = item list
"""


# define functions
def getHealth():
    return userStats[0]


def getStamina():
    return userStats[1]


def getDexterity():
    return userStats[2]


def getMana():
    return userStats[3]


def displayItems():
    itemString = "-----------Items----------- \n"
    loopCounter = 1
    for item in userStats[4]:
        if loopCounter%3 == 0:
            itemString += "\t" + item + "\n"
        else:
            itemString += "\t" + item
        loopCounter += 1
    print(itemString)
    print("---------------------------")
    return


def displayCurrentStats():
    print("------------------")
    print("----User Stats----")
    print("------------------")
    print("  Health = %d  " % getHealth())
    print("  Stamina = %d  " % getStamina())
    print("  Dexterity= %d " % getDexterity())
    print("  Mana = %d    " % getMana())
    print("------------------")


def getTwoDiceSix():
    print("Rolling.....")
    time.sleep(1)
    print("------Dice Roll 6 x 2------")
    rollOne = random.randint(1, 6)
    rollTwo = random.randint(1, 6)
    print("Your Dice rolled %d and %d" % (rollOne, rollTwo))
    print("    The Total is = %d" % (rollOne + rollTwo))
    print("---------------------------")


def getTwenty():
    print("rolling.....")
    time.sleep(1)
    resultText = ""
    result = random.randint(1, 20)
    if result > 14:
        resultText = "Critical Success"
    if result > 15 and result > 5:
        resultText = "Average Result"
    if result < 6:
        resultText = "Critical Failure"
    print("----------------Dice Roll 20--------------------")
    print("Your roll Ended in %d which is a %s" % (result, resultText))
    print("------------------------------------------------")
    return result, resultText


# main routine
print("------------------------------------------------")
print("""           Welcome To Pick A Path
    I wish you good luck on your Adventures""")
print("What Would like to do (S)tats, (I)tems or (M)ove")
print("------------------------------------------------ \n")

userInput = input(">>>").lower()
while True:
    if userInput == "s":
        displayCurrentStats()
    if userInput == "i":
        displayItems()
    if userInput == "m":
        print("You dont Currently Have Legs \n Coming Soon™")
        pass
    print("\n What Would like to do (S)tats, (I)tems or (M)ove \n")
    userInput = input(">>>").lower()



