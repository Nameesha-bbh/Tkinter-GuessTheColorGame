from tkinter import *
from random import *
from tkinter import messagebox


global words

def createWordArray():
    global words
    with open("words.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))

    
root = Tk()
root.title("Guess the color")
root.geometry("600x500")
root.iconbitmap("coloricon.ico")

createWordArray()

wordLabel = Label(root, text="", font=("Helvica",50))
wordLabel.pack(pady=20)

score  = 0
timeLeft = 10

def startGame(event):
    if timeLeft == 10:
        countDown()
        chooseRandomWord()
        scoreLabel.config(text="Score: 0")
    else:
        checkIfCorrect()


def countDown():
    global timeLeft,score
    
    if timeLeft == 0:
        
        inputByUser.config(state="disabled")
        ansButton.config(state="disabled")
        messagebox.showinfo("GAME OVER!!","Time is over and your score is "+ str(score))
        root.destroy()
        
        
        
    if timeLeft > 0:
        timeLeft -= 1
        timeLabel.config(text="Time Left: "+str(timeLeft))
        timeLabel.after(1000,countDown)
        

def chooseRandomWord():
    global words, wordColor
    inputByUser.delete(0,END)
    inputByUser.config(text="")
    
    ansLabel.after(400, lambda: ansLabel.config(text=""))
    
    colors = ['red', 'yellow', 'brown', 'blue', 'orange', 'purple', 'pink', 'black', 'green', 'cyan', 'white', 'navy']
    word = choice(words)
    wordColor = choice(colors)
    wordLabel.config(text=word, fg=str(wordColor))

def checkIfCorrect():
    global timeLeft
    global score
    
    if timeLeft == 10:
        pass
    elif timeLeft > 0:
        inputByUser.focus_set()
        if wordColor.lower() == inputByUser.get().lower():
            score += 1
            ansLabel.config(text="Correct!")
        else:
            ansLabel.config(text="Incorrect!")
        scoreLabel.config(text="Score: "+str(score))
        chooseRandomWord()

scoreLabel = Label(root, text="Press Enter to start the game",font=("Helvetica",24))
scoreLabel.pack(pady=5)

timeLabel = Label(root, text="TimeLeft: "+str(timeLeft),font=("Helvetica",12))
timeLabel.pack(pady=5)

inputByUser = Entry(root, font=("Helvetica",25))
inputByUser.pack(pady=20)

myFrame = Frame(root)
myFrame.pack(pady=20)


ansButton = Button(myFrame, text="Answer", command=checkIfCorrect)
ansButton.grid(row=0, column=1, padx=10)

ansLabel = Label(root, text="", font=("Helvetica",20))
ansLabel.pack(pady=20)

inputByUser.focus_set()

root.bind('<Return>', startGame)

root.mainloop()

