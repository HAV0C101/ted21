# ProgrammingProject_V1.3
# Cory Keastpither

"""
Changelog
v2.2
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
def checkStop():
    return app.yesNoBox("Confirm Exit", "Are you sure you want to quit the game?")


def printBoard():
    # mapString = ""
    LoC = 0
    gridRow = 0
    gridColum = 0
    for line in Board:
        # mapLine = ""
        for character in line:
            print("added new image : " + "Board" + str(gridColum) + "," + str(gridRow))
            if character == "#":
                app.addImage("Board" + str(gridColum) + "," + str(gridRow), "trash.gif", gridRow, gridColum)

            elif character == "X":
                app.addImage("Board" + str(gridColum) + "," + str(gridRow), "Charater.gif", gridRow, gridColum)

            else:
                app.addImage("Board" + str(gridColum) + "," + str(gridRow), "grass.gif", gridRow, gridColum)

            gridColum += 1
            LoC += 1
        gridRow += 1
        gridColum = 0
        # mapLine += character + "        "
        # mapString += mapLine + "" + "\n\n"
    # return mapString


def placeEnemys():
    for i in range(1, 4):
        Board[random.randint(0, 10)][random.randint(0, 10)] = "@"


def placeTrash():
    for i in range(1, 8):
        Board[random.randint(0, 10)][random.randint(0, 10)] = "#"


def launch(win):
    app.showSubWindow(win)


def createFight():
    app.destroySubWindow("Fight")
    enemyNames = [["Dragon", "Orc", "Werewolf"], ["Of Trash", "Of Death", "Of Fire"]]
    enemyHealth = random.randint(30, 100)
    global userStats
    enemyName = enemyNames[0][random.randint(0, 2)] + " " + enemyNames[1][random.randint(0, 2)]
    windowName = "Fight"
    app.startSubWindow(windowName, modal=True)
    app.startLabelFrame("Fight")
    app.addLabel(windowName, "You came across a " + enemyName)
    app.stopLabelFrame()
    app.stopSubWindow()
    app.showSubWindow(windowName)


def keyPress(key):
    global curTrash
    if key == "<Up>":
        prevLoc = [curLoc[0], curLoc[1]]
        Board[prevLoc[0]][prevLoc[1]] = "O"
        curLoc[0] = curLoc[0] - 1

        if curLoc[0] < 0:
            curLoc[0] = prevLoc[0]
            print("Hit Board Bound")
            return
        if Board[curLoc[0]][curLoc[1]] == "@":
            createFight()
        if Board[curLoc[0]][curLoc[1]] == "#":
            print("Trash collected")
            curTrash += 1
            app.setLabel("Statistics",
                         "Your current health is: " + str(userStats[0]) + "\nYour current trash is: " + str(curTrash))
        Board[curLoc[0]][curLoc[1]] = "X"
        print("Previous Location: " + str(prevLoc) + "\n New Location: " + str(curLoc))
        app.setImage("Board" + str(curLoc[0]) + "," + str(curLoc[1]), "Charater.gif")
        app.setLabel("Board", printBoard())
    if key == "<Down>":
        prevLoc = [curLoc[0], curLoc[1]]
        Board[prevLoc[0]][prevLoc[1]] = "O"
        curLoc[0] = curLoc[0] + 1
        if curLoc[0] > 10:
            curLoc[0] = prevLoc[0]
            print("Hit Board Bound")
            return
        if Board[curLoc[0]][curLoc[1]] == "@":
            createFight()
        if Board[curLoc[0]][curLoc[1]] == "#":
            print("Trash collected")
            curTrash += 1
            app.setLabel("Statistics",
                         "Your current health is: " + str(userStats[0]) + "\nYour current trash is: " + str(curTrash))
        Board[curLoc[0]][curLoc[1]] = "X"
        print("Previous Location: " + str(prevLoc) + "\n New Location: " + str(curLoc))
        app.setLabel("Board", printBoard())
    if key == "<Right>":
        prevLoc = [curLoc[0], curLoc[1]]
        Board[prevLoc[0]][prevLoc[1]] = "O"
        curLoc[1] = curLoc[1] + 1
        if curLoc[1] > 10:
            curLoc[1] = prevLoc[1]
            print("Hit Board Bound")
            return
        if Board[curLoc[0]][curLoc[1]] == "@":
            createFight()
        if Board[curLoc[0]][curLoc[1]] == "#":
            print("Trash collected")
            curTrash += 1
            app.setLabel("Statistics",
                         "Your current health is: " + str(userStats[0]) + "\nYour current trash is: " + str(curTrash))
        Board[curLoc[0]][curLoc[1]] = "X"
        print("Previous Location: " + str(prevLoc) + "\n New Location: " + str(curLoc))
        app.setLabel("Board", printBoard())
    if key == "<Left>":
        prevLoc = [curLoc[0], curLoc[1]]
        Board[prevLoc[0]][prevLoc[1]] = "O"
        curLoc[1] = curLoc[1] - 1
        if curLoc[1] < 0:
            curLoc[1] = prevLoc[1]
            print("Hit Board Bound")
            return
        if Board[curLoc[0]][curLoc[1]] == "@":
            createFight()
        if Board[curLoc[0]][curLoc[1]] == "#":
            print("Trash collected")
            curTrash += 1
            app.setLabel("Statistics",
                         "Your current health is: " + str(userStats[0]) + "\nYour current trash is: " + str(curTrash))
        Board[curLoc[0]][curLoc[1]] = "X"
        print("Previous Location: " + str(prevLoc) + "\n New Location: " + str(curLoc))
        app.setLabel("Board", printBoard())


# Create Board
Board[5][5] = "X"
placeTrash()
placeEnemys()

# Setup GUI

app = gui("Epic Quest of Trash", "1000x600")
app.setImageLocation("assets")
# app.setResizable(canResize=False)
# app.setSticky("NEW")
# app.setStretch("COLUMN")
print(curdir + "/assets/logo.png")
app.setIcon("logo.png")
app.setStopFunction(checkStop)

# Bind Keys
app.bindKey("<Up>", keyPress)
app.bindKey("<Down>", keyPress)
app.bindKey("<Left>", keyPress)
app.bindKey("<Right>", keyPress)

# User Inventory
app.startLabelFrame("Inventory", row=0, column=0, rowspan=4)
app.addLabel("test")
app.stopLabelFrame()

enemyNames = [["Dragon", "Orc", "Werewolf"], ["Of Trash", "Of Death", "Of Fire"]]
enemyHealth = random.randint(30, 100)

enemyName = enemyNames[0][random.randint(0, 2)] + " " + enemyNames[1][random.randint(0, 2)]
windowName = "Fight"
app.startSubWindow(windowName, modal=True)
app.startLabelFrame("Fight")
app.addLabel(windowName, "You came across a " + enemyName)
app.stopLabelFrame()
app.stopSubWindow()
# Board
# app.addLabel("Board", printBoard(), 0, 1, 2, 2)

# app.addButton('QUIT', app.stop)
# User Stats
app.startLabelFrame("Stats", row=4, column=0, colspan=6, rowspan=4
                    )
app.addLabel("Statistics", "Your current health is: " + str(userStats[0]) + "\nYour current trash is: " + str(curTrash))
# app.addLabel("CurTrash", "Your current trash is: " + str(curTrash))
# app.addLabel("CurHealth", "Your current health is: " + str(userStats[0]))
app.stopLabelFrame()
app.startLabelFrame("board", row=0, column=6, colspan=8, rowspan=6)
printBoard()
# app.addLabel("Board Zone")
app.setPadding([0,0])
app.setInPadding([20,20])
app.stopLabelFrame()
app.startLabelFrame("Messages", row=10, colspan=12, rowspan=2)
app.addLabel("Message Zone")
app.stopLabelFrame()
app.go()
