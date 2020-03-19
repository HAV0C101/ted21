# 20200304 riddle for door
# Thorne Cooper

# libaries
import random

# variables

# |0 question | 1 possible |2 possible |3 Answer A/B
riddleQs = [
    ["The cake is a?", "Lie", "delishious cake", "A"],
    ["who am i?", "a riddle guy", "protecter of this door", "B"],
    ["who am i?", "a riddle guy", "protecter of this door", "B"]
]


# functions
def displayQuestion():
    question = random.choice(riddleQs)
    print(question[0])
    print("A: %s" % question[1])
    print("B: %s" % question[2])
    userInput = input(">>> ")
    if userInput.upper() == question[3]:
        print("correct")
        return True
    else:
        print("incorrect")
        return False

# testing
# displayQuestion()
