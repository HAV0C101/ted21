# ProgrammingProject_V2.6
# Cory Keastpither

"""
Changelog
v2.6
reworked Board and created GUI

"""

# imports
import random
from os import system, name, curdir
from appJar import gui

# region variables
messageString = "No Messages Yet!"
curTrash = 0
userStats = [100,
             True,
             ["Sword Of Rebellion", "Axe Of Plenty"],
             ["Potion of healing", "Potion of strength", "Potion of luck"]
             ]
# 0 = health 1 = isAlive 2 = Inventory 3 = potions
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


# endregion


# region functions
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
            print("added new image : " + "Board" + str(gridRow) + "," + str(gridColum))
            if character == "#":
                app.addImage("Board" + str(gridRow) + "," + str(gridColum), "trash.gif", gridRow, gridColum)

            elif character == "X":
                app.addImage("Board" + str(gridRow) + "," + str(gridColum), "Charater.gif", gridRow, gridColum)

            else:
                app.addImage("Board" + str(gridRow) + "," + str(gridColum), "grass.gif", gridRow, gridColum)

            gridColum += 1
            LoC += 1
        gridRow += 1
        gridColum = 0
        # mapLine += character + "        "
        # mapString += mapLine + "" + "\n\n"
    # return mapString


def placeEnemys():
    for i in range(0, 4):
        Board[random.randint(0, 10)][random.randint(0, 10)] = "@"


def placeTrash():
    for i in range(0, 8):
        Board[random.randint(0, 10)][random.randint(0, 10)] = "#"


def launch(win):
    app.showSubWindow(win)


def createFight():
    app.destroySubWindow("Fight")
    enemyNames = [["Dragon", "Orc", "Werewolf"], ["Of ", "Of Death", "Of Fire"]]
    enemyHealth = random.randint(30, 100)
    global userStats
    enemyName = enemyNames[0][random.randint(0, 2)] + " " + enemyNames[1][random.randint(0, 2)]
    global messageString
    if messageString == "No Messages Yet!":
        messageString = "You have come accross a " + enemyName
        app.setLabel("Message Label", messageString)
    else:
        messageString = "You have come accross a " + enemyName
        app.setLabel("Message Label", messageString)

    windowName = "Fight"
    app.startSubWindow(windowName, modal=True)
    app.setSize(400, 400)
    app.setStretch("COLUMN")
    app.setSticky("NEW")
    if not enemyName.find("Dragon"):
        app.addImage("Dragonn","dragon.gif")
    app.startLabelFrame("Fight")
    app.addLabel(windowName, "You came across a " + enemyName)
    app.stopLabelFrame()
    app.stopSubWindow()
    app.showSubWindow(windowName)


def press(btn):
    print(btn)


def keyPress(key):
    global messageString
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
            if messageString == "No Messages Yet!":
                messageString = "You Picked up a peice of trash!"
                app.setLabel("Message Label", messageString)
            else:
                messageString = "You Picked up a peice of trash!"
                app.setLabel("Message Label", messageString)
            print("Trash collected")
            curTrash += 1
            # app.setLabel("Statistics",
            #              "Your current health is: " + str(userStats[0]) + "\nYour current trash is: " + str(curTrash))
        Board[curLoc[0]][curLoc[1]] = "X"
        print("Previous Location: " + str(prevLoc) + "\n New Location: " + str(curLoc))
        app.setImage("Board" + str(curLoc[0]) + "," + str(curLoc[1]), "Charater.gif")
        app.setImage("Board" + str(prevLoc[0]) + "," + str(prevLoc[1]), "grass.gif")
        # app.setLabel("Board", printBoard())
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
            if messageString == "No Messages Yet!":
                messageString = "You Picked up a peice of trash!"
                app.setLabel("Message Label", messageString)
            else:
                messageString = "You Picked up a peice of trash!"
                app.setLabel("Message Label", messageString)
            print("Trash collected")
            curTrash += 1
            # app.setLabel("Statistics",
            #              "Your current health is: " + str(userStats[0]) + "\nYour current trash is: " + str(curTrash))
        Board[curLoc[0]][curLoc[1]] = "X"
        print("Previous Location: " + str(prevLoc) + "\n New Location: " + str(curLoc))
        app.setImage("Board" + str(curLoc[0]) + "," + str(curLoc[1]), "Charater.gif")
        app.setImage("Board" + str(prevLoc[0]) + "," + str(prevLoc[1]), "grass.gif")
        # app.setLabel("Board", printBoard())
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
            if messageString == "No Messages Yet!":
                messageString = "You Picked up a peice of trash!"
                app.setLabel("Message Label", messageString)
            else:
                messageString = "You Picked up a peice of trash!"
                app.setLabel("Message Label", messageString)
            print("Trash collected")
            curTrash += 1
            # app.setLabel("Statistics",
            #              "Your current health is: " + str(userStats[0]) + "\nYour current trash is: " + str(curTrash))
        Board[curLoc[0]][curLoc[1]] = "X"
        print("Previous Location: " + str(prevLoc) + "\n New Location: " + str(curLoc))
        app.setImage("Board" + str(curLoc[0]) + "," + str(curLoc[1]), "Charater.gif")
        app.setImage("Board" + str(prevLoc[0]) + "," + str(prevLoc[1]), "grass.gif")
        # app.setLabel("Board", printBoard())
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
            if messageString == "No Messages Yet!":
                messageString = "You Picked up a peice of trash!"
                app.setLabel("Message Label", messageString)
            else:
                messageString = "You Picked up a peice of trash!"
                app.setLabel("Message Label", messageString)
            print("Trash collected")
            curTrash += 1
            # app.setLabel("Statistics",
            #              "Your current health is: " + str(userStats[0]) + "\nYour current trash is: " + str(curTrash))
        Board[curLoc[0]][curLoc[1]] = "X"
        print("Previous Location: " + str(prevLoc) + "\n New Location: " + str(curLoc))
        app.setImage("Board" + str(curLoc[0]) + "," + str(curLoc[1]), "Charater.gif")
        app.setImage("Board" + str(prevLoc[0]) + "," + str(prevLoc[1]), "grass.gif")
        # app.setLabel("Board", printBoard())


# endregion


# region Setup

# Setup Board
Board[5][5] = "X"
placeTrash()
placeEnemys()

# Setup GUI

app = gui("Epic Quest of Something", "1000x540")
app.setImageLocation("assets")
app.setResizable(canResize=False)
app.setStretch("COLUMN")
app.setSticky("NEW")
print(curdir + "/assets/logo.png")
app.setIcon("logo.png")
app.setStopFunction(checkStop)

# Bind Keys
app.bindKey("<Up>", keyPress)
app.bindKey("<Down>", keyPress)
app.bindKey("<Left>", keyPress)
app.bindKey("<Right>", keyPress)

app.startSubWindow("Fight", modal=True)
app.stopSubWindow()
# endregion


# region User Inventory
app.startLabelFrame("Inventory", row=0, column=0, rowspan=9)
InvetoryString = "Items: \n"
for Item in userStats[2]:
    InvetoryString = InvetoryString + Item + "\n"
InvetoryString += "\nPotions: \n"
for Potion in userStats[3]:
    InvetoryString = InvetoryString + Potion + "\n"
app.addLabel("InventoryLabel", InvetoryString)
app.stopLabelFrame()
# endregion


# region HealthBar
app.addSplitMeter("Health", row=9, column=0, colspan=6, rowspan=1)
app.setMeterFill("Health", ["green", "red"])
app.setMeter("Health", 70)
# endregion


# region Board
app.startLabelFrame("board", row=0, column=6, colspan=8, rowspan=10)
app.setBg("#1a6b2e")
printBoard()
app.setPadding([0, 0])
app.setInPadding([20, 20])
app.stopLabelFrame()
# endregion


# region Actions
app.startLabelFrame("Actions", row=13, colspan=8)
app.addButton("test", press, column=0, row=0)
app.addButton("Create Fight", createFight, column=1, row=0)
app.stopLabelFrame()
# endregion


# region Message Zone
app.startLabelFrame("Messages", row=14, colspan=12, rowspan=4)
app.addLabel("Message Label", messageString)
app.stopLabelFrame()
app.setBg("#1a6b2e")
# endregion

app.go()
