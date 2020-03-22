# ProgrammingProject_V1.2
# Cory Keastpither

"""
Changelog
v1.2
Begun Board

"""

# imports
import random
from os import system, name

# variables
userStats = []
isAlive = True
health = 100
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


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def printBoard():
    mapString = ""
    for line in Board:
        mapLine = "\t\t\t"
        for character in line:
            mapLine += character+"   "
        mapString += mapLine+"\n"
    return mapString


# main routine


Board[5][5] = "X"
# for i in range(len(Board)):
#     print(Board[i])
printBoard()
while True:
    userInput = input("Which direction do you wanna move in: ")
    if userInput.lower() == "n":
        Board[curLoc[0]][curLoc[1]] = "*"
        curLoc[0] = curLoc[0] - 1
        print(curLoc)
        Board[curLoc[0]][curLoc[1]] = "X"
        clear()
        printBoard()
    if userInput.lower() == "s":
        Board[curLoc[0]][curLoc[1]] = "*"
        curLoc[0] = curLoc[0] + 1
        Board[curLoc[0]][curLoc[1]] = "X"
        clear()
        printBoard()
    if userInput.lower() == "e":
        Board[curLoc[0]][curLoc[1]] = "*"
        curLoc[1] = curLoc[1] + 1
        Board[curLoc[0]][curLoc[1]] = "X"
        clear()
        printBoard()
    if userInput.lower() == "w":
        Board[curLoc[0]][curLoc[1]] = "*"
        curLoc[1] = curLoc[1] - 1
        Board[curLoc[0]][curLoc[1]] = "X"
        clear()
        print(printBoard())
