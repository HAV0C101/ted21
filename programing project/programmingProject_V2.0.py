# ProgrammingProject_V2.0
# Cory Keastpither

"""
Changelog
v2.0
reworked Board and created GUI

"""

# imports
import random
from os import system, name, curdir
from appJar import gui

# variables
curTrash = 0
userStats = [100, True]
# 0 = health 1 = isAlive
curLoc = [5, 5]
Board = [
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
]


# functions
def printBoard():
    mapString = ""
    for line in Board:
        mapLine = ""
        for character in line:
            mapLine += character + "        "
        mapString += mapLine + "" + "\n\n"
    return mapString


def placeEnemys():
    for i in range(1, 4):
        Board[random.randint(0, 10)][random.randint(0, 10)] = "@"


def placeTrash():
    for i in range(1, 8):
        Board[random.randint(0, 10)][random.randint(0, 10)] = "#"


def keyPress(key):
    if key == "<Up>":
        Board[curLoc[0]][curLoc[1]] = "O"
        curLoc[0] = curLoc[0] - 1
        print(curLoc)
        Board[curLoc[0]][curLoc[1]] = "X"
        app.setLabel("Board", printBoard())
    if key == "<Down>":
        Board[curLoc[0]][curLoc[1]] = "O"
        curLoc[0] = curLoc[0] + 1
        print(curLoc)
        Board[curLoc[0]][curLoc[1]] = "X"
        app.setLabel("Board", printBoard())
    if key == "<Right>":
        Board[curLoc[0]][curLoc[1]] = "O"
        curLoc[1] = curLoc[1] + 1
        print(curLoc)
        Board[curLoc[0]][curLoc[1]] = "X"
        app.setLabel("Board", printBoard())
    if key == "<Left>":
        Board[curLoc[0]][curLoc[1]] = "O"
        curLoc[1] = curLoc[1] - 1
        print(curLoc)
        Board[curLoc[0]][curLoc[1]] = "X"
        app.setLabel("Board", printBoard())


# Create Board
Board[5][5] = "X"
placeTrash()
placeEnemys()

# Setup GUI
app = gui("Epic Quest of life", "1200x800")
app.setResizable(canResize=False)
app.setSticky("news")
app.setExpand("both")
print(curdir + "/assets/logo.png")
app.setIcon(curdir + "/assets/logo.png")

# Bind Keys
app.bindKey("<Up>", keyPress)
app.bindKey("<Down>", keyPress)
app.bindKey("<Left>", keyPress)
app.bindKey("<Right>", keyPress)

# User Inventory
app.startLabelFrame("Inventory")

app.stopLabelFrame()

# Board
app.addLabel("Board", printBoard(), 0, 1, 2, 2)

# User Stats
app.startLabelFrame("Stats")
app.addLabel("CurTrash", "Your current trash is: " + str(curTrash))
app.addLabel("CurHealth", "Your current health is: " + str(userStats[0]))
app.stopLabelFrame()

# Start App
app.go()
