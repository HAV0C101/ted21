# 24/02/2020 pickApath_V1.0.py
# Cory Keastpither

"""
*********************************************
Change Log V1.1
- Setup Game
-
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
getTwenty()
getTwoDiceSix()
displayCurrentStats()



