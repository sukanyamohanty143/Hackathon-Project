from tkinter import *
import random
frame = Tk()

frame.geometry("500x500")
frame.title("guess the number")

global ability
ability = random.randint(1,100)
print (ability)

def retrieve_input():
    input = t1.get("1.0",'end-1c')
    return input

def startFunction():
    global t2
    frame.destroy()
    frame2 = Tk()

    frame2.geometry("500x247")
    frame2.title("guess the number")

    l1 = Label(text="The Number Guessing Game", font=("Helvetica", 27))
    l1.place(x=10, y=10)

    l2 = Label(text="Guess your number here (0-100)")
    l2.place(x=10, y=100)

    t1 = Entry(width= 5)
    t1.place(x= 10, y= 124)

    # 
    # l3.place(x=10, y=190)

    # t2 = Entry(width= 15)
    # t2.place(x= 10, y= 214)

    def numberFunction():
        global ability,t2
        if int(t1.get()) == ability:
            l3 = Label(text="correct")
            l3.place(x=10, y=220)
        if int(t1.get()) > ability:
            l4 = Label(text="Guess Lower")
            l4.place(x=10, y=220)
        if int(t1.get()) < ability:
            l5 = Label(text="Guess Higher")
            l5.place(x=10, y=220)

    b1 = Button(text="Enter", width= 5, height= 1, command= numberFunction)
    b1.place(x= 10, y= 150)



b1 = Button(text="START", width=12, height=2, command=startFunction)
b1.place(x=210, y=210)

frame.mainloop()