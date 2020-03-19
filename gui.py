# import the library
from appJar import gui
import pickApathQuiz

# var
quizPos = 0


# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    if button == "A" or button == "B":
        if button == pickApathQuiz.riddleQs[quizPos][3]:
            app.setLabel("question", "correct")
        else:
            app.setLabel("question", "wrong")
    if button == "Next":
        displayQuestion()


def displayQuestion():
    global quizPos
    app.setLabel("question", pickApathQuiz.riddleQs[quizPos][0])
    app.setButton("A", "A: " + pickApathQuiz.riddleQs[quizPos][1])
    app.setButton("B", "B: " + pickApathQuiz.riddleQs[quizPos][2])
    if quizPos < len(pickApathQuiz.riddleQs) - 1:
        quizPos += 1


# create a GUI variable called app
app = gui("Quiz Window", "800x200")
app.setBg("orange")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later


app.addLabel("title", "Welcome to Quiz")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")

app.addLabel("question", "Questions Go here")
app.setLabelBg("question", "pink")

# app.addLabel("awnser1", "Awnser Go here")
# app.setLabelBg("awnser1", "pink")
#
# app.addLabel("awnser2", "Awnser Go here")
# app.setLabelBg("awnser2", "pink")
# link the buttons to the function called press
app.addButtons(["A", "B", "Next", "Cancel"], press)
# start the GUI
app.go()
