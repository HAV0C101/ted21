# 26/02/2020 pickApath_V1.2.py
# Cory Keastpither

"""
*********************************************
Change Log V1.2
- Added Fight Sequence
- Added Run physics
- Added Fighting
*********************************************
"""

# imports

import random
import time

# declare Vars
enemyNames = [["Frost", "Fire", "Earth"], ["Dragon", "Giant", "Phoenix"]]
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
        if loopCounter % 3 == 0:
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
    return rollTwo + rollOne


def createEnemy():
    name = enemyNames[0][random.randint(0, 2)] + " " + enemyNames[1][random.randint(0, 2)]
    HP = random.randint(20, 100)
    print("Youve Stumbled Across a %s With %d Health" % (name, HP))
    return [name, HP]


def fightEnemy():
    enemy = createEnemy()
    name = enemy[0]
    enemyHP = enemy[1]
    print("What do you wish to do (F)ight (R)un (C)heck Stats or (H)eal")
    userInput = input(">>>").lower()
    while enemyHP > 1:
        if userInput == "c":
            displayCurrentStats()
        if userInput == "r":
            rand = random.randint(0, 1)
            if rand == 1:
                print("You Successfully Run away")
                break
            if rand == 0:
                userHealthTakeOff = random.randint(5, 20)
                print("You Were Unable to Run And lost %d HP in the Process" % userHealthTakeOff)
                userStats[0] -= userHealthTakeOff
        if userInput == "f":
            if enemyHP > 20:
                takeOff = random.randint(5, 30)
                enemyHP -= takeOff
                print("You Took %s HP off the enemy Successfully" % takeOff)
                print("%s's HP: %d" % (name, enemyHP))
                if enemyHP == 0:
                    print("You Have Successfully Defeated %s" % name)
                    break
            else:
                healthTakeOff = enemyHP
                enemyHP -= enemyHP
                print("You Took %s HP off the enemy Successfully" % healthTakeOff)
                print("%s's HP: %d" % (name, enemyHP))
                if enemyHP == 0:
                    print("You Have Succsessfully Defeated %s" % name)
                    break
        if userInput == "h":
            print("You dont Currently Have That Ability \n Coming Soon™")
            pass
        print("\n What do you wish to do (F)ight (R)un or (H)eal \n")
        userInput = input(">>>").lower()


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
print("What Would you like to do (S)tats, (I)tems or (M)ove")
print("------------------------------------------------ \n")

userInput = input(">>>").lower()
while True:
    if userInput == "s":
        displayCurrentStats()
    if userInput == "i":
        displayItems()
    if userInput == "m":
        # print("You dont Currently Have Legs \n Coming Soon™")
        print("You were Unable to move As There was an enemy Blocking your way")
        fightEnemy()
    print("\n What Would you like to do (S)tats, (I)tems or (M)ove \n")
    userInput = input(">>>").lower()


