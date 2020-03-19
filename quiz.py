# 190220 Quiz
# Cory Keastpither


questions = []
i = 0
score = 0
test = ""
# questions
questions.append(["What color is my shirt", "Red", "Yellow", "Orange", "Blue", "D"])
questions.append(["What Does this mean ==", "Equal To Or Less than", "Less Than", "Equal", "More Than", "C"])
questions.append(["Who made this Quiz", "Aidan", "Mr Mcleod", "Cory", "Thorne", "C"])
questions.append(["What is the meaning of life", "42", "Nothing", "Everything", "Love", "A"])


# define functions

def hasScore(QuestionNumber):
    if test == questions[QuestionNumber][5]:
        return "true"

    else:
        return "false"


def printQuestion(QuestionNumber):
    print(questions[QuestionNumber][0])
    print("A: %s" % questions[QuestionNumber][1])
    print("B: %s" % questions[QuestionNumber][2])
    print("C: %s" % questions[QuestionNumber][3])
    print("D: %s" % questions[QuestionNumber][4])


def answerChecker(QuestionNumber):
    global test
    userInput = input("Whats Your Awnser: ")
    test = userInput
    if userInput.upper() == questions[QuestionNumber][5]:
        print("correct")

    else:
        print("Incorrect")


# main
for i in range(len(questions)):
    printQuestion(i)
    answerChecker(i)
    if hasScore(i) == "true":
        score += 1
        print("Current Score: %s" % score)
print("Your Total Score was %d" % score)
