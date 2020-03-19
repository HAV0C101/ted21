# 11022020 Cory Keastpither
# subtraction game

#imports
import random
#set Constants
total = random.randint(5,20)

#Forever loop
while True:
    N = total%3#computer start
    if N > 0:
        total -= N
    else:
        total -= 1
    print("Puter took off %d" %N)
    if total == 0: # if computer wins
        print("I Win")
        break#end game
    userInput = int(input("1 or 2: "))#user start
    while userInput < 1 or userInput > 2:
        print("wrong")
        userInput = int(input("1 or 2: "))
    total -= userInput
    print("Total is now %d" %total)
    if total == 0:
        print("You Win")
        break