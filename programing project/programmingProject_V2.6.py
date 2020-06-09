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
import time

# region variables
enemyHealth = 0

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
def damage(amount):
    global userStats
    userStats[0] -= int(amount)
    print(str(userStats[0]))
    app.setMeter("Health", userStats[0])
    if userStats[0] <= 0:
        app.unbindKey("<Up>")
        app.unbindKey("<Down>")
        app.unbindKey("<Left>")
        app.unbindKey("<Right>")
        app.startSubWindow("Game Over", modal=True)
        app.setSize(400, 200)
        app.addLabel("Game Over")
        app.addButton("Quit Game", exit)
        app.stopSubWindow()
        app.showSubWindow("Game Over")


def checkStop():
    return app.yesNoBox("Confirm Exit", "Are you sure you want to quit the game?")


def printBoard():
    LoC = 0
    gridRow = 0
    gridColum = 0
    for line in Board:
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


def placeEnemys():
    for i in range(0, 4):
        Board[random.randint(0, 10)][random.randint(0, 10)] = "@"


def placeTrash():
    for i in range(0, 8):
        Board[random.randint(0, 10)][random.randint(0, 10)] = "#"


def launch(win):
    app.showSubWindow(win)


def createFight():
    global enemyHealth
    app.destroySubWindow("Fight")
    enemyNames = [["Dragon", "Orc", "Werewolf"], ["Of Something", "Of Death", "Of Fire"]]
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
    app.setSize(400, 500)
    app.setStretch("COLUMN")
    app.setSticky("NEW")
    if not enemyName.find("Dragon"):
        app.startLabelFrame("Dragon", colspan=3)
        app.addImage("Dragon", "dragon.gif")
        app.stopLabelFrame()
    if not enemyName.find("Werewolf"):
        app.startLabelFrame("Werewolf", colspan=3)
        app.addImage("werewolf", "werewolf.gif")
        app.stopLabelFrame()
    app.startLabelFrame("Fight", colspan=2)
    app.addLabel("Fight Message", "You came across a " + enemyName)
    app.stopLabelFrame()
    app.addLabel("Your Health:", row=2, column=0)
    app.addSplitMeter("Your Health", row=3, column=0)
    app.setMeterFill("Your Health", ["green", "red"])
    app.setMeter("Your Health", userStats[0])
    app.addLabel("Enemy Health:", row=2, column=1)
    app.addSplitMeter("Enemy Health", row=3, column=1)
    app.setMeterFill("Enemy Health", ["green", "red"])
    app.setMeter("Enemy Health", enemyHealth)
    app.addButton("Fight", press, column=0, row=4)
    app.addButton("Defend", press, column=0, row=5)
    app.addButton("Heal", press, column=1, row=4)
    app.addButton("Run", press, column=1, row=5)
    app.stopSubWindow()
    app.showSubWindow(windowName)


def press(btn):
    global enemyHealth
    global userStats

    def enemyAttack():
        enemyChance = random.randint(0, 6)
        # time.sleep(2)
        if enemyChance > 2:
            attackDamage = random.randint(10, 30)
            damage(attackDamage)
            app.setLabel("Message Label", "Enemy attacked you for " + str(attackDamage) + "hp")
            app.setLabel("Fight Message", "Enemy attacked you for " + str(attackDamage) + "hp")
            app.setMeter("Your Health", userStats[0])
        if enemyChance <= 2:
            app.setLabel("Message Label", "Enemy attack failed")
            app.setLabel("Fight Message", "Enemy attack failed")

    if btn == "Fight":
        chance = random.randint(0, 10)
        if chance > 4:
            print("succsses")
            attackAmount = random.randint(10, 30)
            enemyHealth -= attackAmount
            app.setLabel("Message Label", "Successfully hit Enemy For " + str(attackAmount) + "hp")
            app.setLabel("Fight Message", "Successfully hit Enemy For " + str(attackAmount) + "hp")
            app.setMeter("Enemy Health", enemyHealth)
            if enemyHealth <= 0:
                app.setLabel("Message Label", "Killed Enemy")
                app.setLabel("Fight Message", "Killed Enemy")
                app.hideSubWindow("Fight")
            if enemyHealth >= 0:
                enemyAttack()
        if chance <= 4:
            print("Attack failed")
            app.setLabel("Message Label", "Attack Failed")
            app.setLabel("Fight Message", "Attack Failed")
            enemyAttack()
    if btn == "Heal":
        chance = random.randint(0, 10)
        if chance > 4:
            app.setLabel("Message Label", "Successfully Healed")
            app.setLabel("Fight Message", "Successfully Healed")
            userStats[0] = 100
            app.setMeter("Your Health", userStats[0])
            app.setMeter("Health", userStats[0])
            enemyAttack()
        if chance <= 4:
            app.setLabel("Message Label", "Unable to heal")
            app.setLabel("Fight Message", "Unable to heal")
            enemyAttack()
    if btn == "Run":
        chance = random.randint(0, 10)
        if chance > 4:
            app.setLabel("Message Label", "Successfully Run")
            app.hideSubWindow("Fight")
        if chance <= 4:
            app.setLabel("Message Label", "Unable to Run")
            app.setLabel("Fight Message", "Unable to Run")
            enemyAttack()
    if btn == "Defend":
        pass


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
# app.setStopFunction(checkStop)

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
app.setMeter("Health", userStats[0])
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
# app.addButton("damage", damage, column=2, row=0)
app.stopLabelFrame()
# endregion


# region Message Zone
app.startLabelFrame("Messages", row=14, colspan=12, rowspan=4)
app.addLabel("Message Label", messageString)
app.stopLabelFrame()
app.setBg("#1a6b2e")
# endregion

app.go()
