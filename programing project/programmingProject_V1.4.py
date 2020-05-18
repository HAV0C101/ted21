# ProgrammingProject_V1.3
# Cory Keastpither

"""
Changelog
v1.4
Started fights

"""

# imports
import random
from os import system, name

# variables
curTrash = 0
userStats = [100, True]
# 0 = health 1 = isAlive
curLoc = [5, 5]
Board = [
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
]


# functions
def search(trash):
    pass


def startfight():
    enemyHealth = 100
    print("What do you want to do?")
    print("Run: R")
    print("Attack: A")
    print("Defend: D")
    userFightInput = input(">>>")
    if userFightInput.lower() == "r":
        chance = random.randint(0, 1)
        if chance == 0:
            print("You successfully ran away")
        if chance == 1:
            print("you were unable to run")
    if userFightInput.lower() == "a":
        print("You attack the trash monster with your sword")
        take_off = random.randint(0, 40)
        if take_off == 0:
            "You were unsuccessful in attacking the enemy"
            enemy_attack = random.randint(0, 40)
            if enemy_attack == 0:
                print("Enemy was unable to hit you")
            else:
                print("Ememy took off %s health from you" % enemy_attack)
                userStats[0] -= enemy_attack
                print("Your current health is %d" % userStats[0])
                if userStats[0] == 0:
                    print("You have died")
                    exit(0)
        else:
            print("you took %d health off the enemy" % take_off)
            enemyHealth -= take_off
            print("enemys health is now %d" % enemyHealth)

    if userFightInput.lower() == "d":
        pass


def placeEnemys():
    for i in range(1, 4):
        Board[random.randint(0, 10)][random.randint(0, 10)] = "@"


def placeTrash():
    for i in range(1, 8):
        Board[random.randint(0, 10)][random.randint(0, 10)] = "#"


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def printBoard():
    mapString = "____________________________________\n"
    for line in Board:
        mapLine = "| "
        for character in line:
            mapLine += character + "  "
        mapString += mapLine + "|" + "\n"
    return mapString + "|----------------------------------|\n" + "|         Current Trash: " + str(curTrash) + \
           "         |\n" + "|         Current Health: " + str(userStats[0]) + \
           "      |\n" + "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n"


# main routine


Board[5][5] = "X"
# for i in range(len(Board)):
#     print(Board[i])
placeTrash()
placeEnemys()
print(printBoard())

while True:
    userInput = input("Which direction do you wanna move in: ")
    if userInput.lower() == "w":
        prevloc = [curLoc[0], curLoc[1]]
        curLoc[0] = curLoc[0] - 1
        if Board[curLoc[0]][curLoc[1]] == "#":
            print("Picked Up Trash")
            curTrash += 1
        if Board[curLoc[0]][curLoc[1]] == "@":
            print("You Found an Enemy")
        Board[prevloc[0]][prevloc[1]] = "*"

        Board[curLoc[0]][curLoc[1]] = "X"
        # clear()
        print(printBoard())
    if userInput.lower() == "s":
        prevloc = [curLoc[0], curLoc[1]]
        curLoc[0] = curLoc[0] + 1
        if Board[curLoc[0]][curLoc[1]] == "#":
            print("Picked Up Trash")
            curTrash += 1
        if Board[curLoc[0]][curLoc[1]] == "@":
            print("You Found an Enemy")
            startfight()
        Board[prevloc[0]][prevloc[1]] = "*"

        Board[curLoc[0]][curLoc[1]] = "X"
        # clear()
        print(printBoard())
    if userInput.lower() == "d":
        prevloc = [curLoc[0], curLoc[1]]
        curLoc[1] = curLoc[1] + 1
        if Board[curLoc[0]][curLoc[1]] == "#":
            print("Picked Up Trash")
            curTrash += 1
        if Board[curLoc[0]][curLoc[1]] == "@":
            print("You Found an Enemy")
            startfight()
        Board[prevloc[0]][prevloc[1]] = "*"

        Board[curLoc[0]][curLoc[1]] = "X"
        # clear()
        print(printBoard())
    if userInput.lower() == "a":
        prevloc = [curLoc[0], curLoc[1]]
        curLoc[1] = curLoc[1] - 1
        if Board[curLoc[0]][curLoc[1]] == "#":
            print("Picked Up Trash")

            curTrash += 1
        if Board[curLoc[0]][curLoc[1]] == "@":
            print("You Found an Enemy")
            startfight()
        Board[prevloc[0]][prevloc[1]] = "*"

        Board[curLoc[0]][curLoc[1]] = "X"
        # clear()
        print(printBoard())
