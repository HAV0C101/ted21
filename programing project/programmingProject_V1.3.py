# ProgrammingProject_V1.3
# Cory Keastpither

"""
Changelog
v1.3
Layout
Trash System start

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
    mapString = "___________________________________\n"
    for line in Board:
        mapLine = "|"
        for character in line:
            mapLine += character + "  "
        mapString += mapLine + "|" + "\n"
    return mapString + "|---------------------------------|\n" + "|         Current Trash: " + str(curTrash) + \
           "        |\n" +"|         Current Health: " + str(userStats[0]) + \
           "     |\n" + "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n"


# main routine


Board[5][5] = "X"
# for i in range(len(Board)):
#     print(Board[i])
placeTrash()
print(printBoard())

while True:
    userInput = input("Which direction do you wanna move in: ")
    if userInput.lower() == "w":
        prevloc = [curLoc[0], curLoc[1]]
        curLoc[0] = curLoc[0] - 1
        if Board[curLoc[0]][curLoc[1]] == "#":
            print("Picked Up Trash")
            curTrash += 1
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
        Board[prevloc[0]][prevloc[1]] = "*"

        Board[curLoc[0]][curLoc[1]] = "X"
        # clear()
        print(printBoard())
