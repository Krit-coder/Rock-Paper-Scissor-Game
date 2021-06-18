from tkinter import *
import random


#######################################################################################
def single(name1):
    # Create Object
    root = Tk()

    # Setting the icon of title bar
    root.iconbitmap('d:/rps2.ico')

    # Set title
    root.title("Rock Paper Scissor Game")

    # Computer Value

    computer_value = {
        "0": "Rock",
        "1": "Paper",
        "2": "Scissor"
    }

    # Reset The Game
    def reset_game():
        b1["state"] = "active"
        b2["state"] = "active"
        b3["state"] = "active"
        l5.config(text="")
        l4.config(text="")

    # Disable the Button
    def button_disable():
        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"

    # If player selected rock

    def isrock():
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            match_result = "Match Draw"
        elif c_v == "Scissor":
            match_result = name1 + " Win"
        else:
            match_result = "Computer Win"
        l5.config(text=match_result)
        l4.config(text="Rock      VS     "+c_v)
        button_disable()

    # If player selected paper
    def ispaper():
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Paper":
            match_result = "Match Draw"
        elif c_v == "Scissor":
            match_result = "Computer Win"
        else:
            match_result = name1 + " Win"
        l5.config(text=match_result)
        l4.config(text="Paper      VS     "+c_v)
        button_disable()

    # If player selected scissor
    def isscissor():
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            match_result = "Computer Win"
        elif c_v == "Scissor":
            match_result = "Match Draw"
        else:
            match_result = name1 + " Win"
        l5.config(text=match_result)
        l4.config(text="Scissor      VS     "+c_v)
        button_disable()

    # Add Labels, Frames and Button
    Label(root,
          text="Rock Paper Scissor",
          font="normal 20 bold",
          fg="blue").pack(pady=20)

    frame = Frame(root)
    frame.pack()

    l1 = Label(frame,
               text=name1+"		  ",
               font=10)

    l2 = Label(frame,
               text="VS		  ",
               font="normal 10 bold")

    l3 = Label(frame,
               text="Computer",
               font=10)

    l1.pack(side=LEFT)
    l2.pack(side=LEFT)
    l3.pack()

    l4 = Label(root,
               text="",
               font="normal 20",
               bg="white",
               width=25,
               borderwidth=2,
               relief="solid")
    l4.pack(pady=20)

    l5 = Label(root,
               text="",
               font="normal 20 bold",
               bg="white",
               width=15,
               borderwidth=2,
               relief="solid")
    l5.pack(pady=20)

    frame1 = Frame(root)
    frame1.pack()

    b1 = Button(frame1, text="Rock",
                font=10, width=7,
                command=isrock)

    b2 = Button(frame1, text="Paper ",
                font=10, width=7,
                command=ispaper)

    b3 = Button(frame1, text="Scissor",
                font=10, width=7,
                command=isscissor)

    b1.pack(side=LEFT, padx=10)
    b2.pack(side=LEFT, padx=10)
    b3.pack(padx=10)

    Button(root, text="Reset",
           font=10, fg="red",
           bg="black", command=reset_game).pack(pady=20)

    # Excecute Tkinter
    root.mainloop()
###########################################################################################


###########################################################################################


def multi(name1, name2):
    # Create Object
    root = Tk()

    # Setting the icon of title bar
    root.iconbitmap('d:/rps2.ico')

    # Set title
    root.title("Rock Paper Scissor Game")

    # Player1 intialization

    p1 = ""

    # Reset The Game
    def reset_game():
        b1["state"] = "active"
        b2["state"] = "active"
        b3["state"] = "active"
        b4["state"] = "active"
        b5["state"] = "active"
        b6["state"] = "active"
        l5.config(text="")
        l4.config(text="")

    # Disable the Button
    def button_disable1():
        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"

    def button_disable2():
        b4["state"] = "disable"
        b5["state"] = "disable"
        b6["state"] = "disable"

    # Player1 function

    def play1r():
        global p1
        p1 = "Rock"
        button_disable1()

    def play1p():
        global p1
        p1 = "Paper"
        button_disable1()

    def play1s():
        global p1
        p1 = "Scissor"
        button_disable1()

    # If player2 selected rock
    def isrock():
        global p1
        if p1 == "Rock":
            match_result = "Match Draw"
        elif p1 == "Scissor":
            match_result = name2+" Win"
        else:
            match_result = name1 + " Win"
        l5.config(text=match_result)
        l4.config(text=p1+"        VS         Rock")
        button_disable2()

    # If player2 selected paper
    def ispaper():
        global p1
        if p1 == "Paper":
            match_result = "Match Draw"
        elif p1 == "Scissor":
            match_result = name1 + " Win"
        else:
            match_result = name2+" Win"
        l5.config(text=match_result)
        l4.config(text=p1+"        VS         Paper")
        button_disable2()

    # If player2 selected scissor
    def isscissor():
        global p1
        if p1 == "Rock":
            match_result = name1 + " Win"
        elif p1 == "Scissor":
            match_result = "Match Draw"
        else:
            match_result = name2+" Win"
        l5.config(text=match_result)
        l4.config(text=p1+"        VS         Scissor")
        button_disable2()

    # Add Labels, Frames and Button
    Label(root,
          text="Rock Paper Scissor",
          font="normal 20 bold",
          fg="blue").pack(pady=20)

    frame = Frame(root)
    frame.pack()

    l1 = Label(frame,
               text=name1+"		  ",
               font=10)

    l2 = Label(frame,
               text="VS		  ",
               font="normal 10 bold")

    l3 = Label(frame,
               text=name2,
               font=10)

    l1.pack(side=LEFT)
    l2.pack(side=LEFT)
    l3.pack()

    l4 = Label(root,
               text="",
               font="normal 20",
               bg="white",
               width=25,
               borderwidth=2,
               relief="solid")
    l4.pack(pady=20)

    l5 = Label(root,
               text="",
               font="normal 20 bold",
               bg="white",
               width=15,
               borderwidth=2,
               relief="solid")
    l5.pack(pady=20)

    frame1 = LabelFrame(root, text=name1, pady=10, font=5)
    frame1.pack()

    b1 = Button(frame1, text="Rock",
                font=10, width=7,
                command=play1r)

    b2 = Button(frame1, text="Paper ",
                font=10, width=7,
                command=play1p)

    b3 = Button(frame1, text="Scissor",
                font=10, width=7,
                command=play1s)

    b1.pack(side=LEFT, padx=10)
    b2.pack(side=LEFT, padx=10)
    b3.pack(padx=10)

    frame2 = LabelFrame(root, text=name2, pady=10, font=5)
    frame2.pack()

    b4 = Button(frame2, text="Rock",
                font=10, width=7,
                command=isrock)

    b5 = Button(frame2, text="Paper ",
                font=10, width=7,
                command=ispaper)

    b6 = Button(frame2, text="Scissor",
                font=10, width=7,
                command=isscissor)

    b4.pack(side=LEFT, padx=10)
    b5.pack(side=LEFT, padx=10)
    b6.pack(padx=10)

    Button(root, text="Reset",
           font=10, fg="red",
           bg="black", command=reset_game).pack(pady=20)

    # Excecute Tkinter
    root.mainloop()


##########################################################################################
# Create Object
root = Tk()

# Setting the icon of title bar
root.iconbitmap('d:/rps2.ico')


# Set title
root.title("Rock Paper Scissor Game")


# Set Heading
Label(root,
      text="Rock Paper Scissor",
      font="normal 20 bold",
      fg="red").pack(pady=20)


# Enter name option
n1l = Label(root, text="Enter Player1 Name ", font=5)
n1 = Entry(root, font=5)
n1l.pack(pady=15)
n1.pack()

n2l = Label(root, text="Enter Player2 Name(only in PvP) ", font=5)
n2 = Entry(root, font=5)
n2l.pack(pady=15)
n2.pack(pady=10)

# Making Radio Button
r = IntVar()
Radiobutton(root, text="Player vs Computer",
            font=5, variable=r, value=1).pack()
Radiobutton(root, text="Player vs Player", font=5, variable=r, value=2).pack()


def play(a):
    if a == 1:
        single(n1.get())
    if a == 2:
        multi(n1.get(), n2.get())


# EXit Button
frame3 = Frame(root)
frame3.pack()
Exit1 = Button(frame3, text="Exit", font=5, command=root.quit, bg="red")
Play = Button(frame3, text="Play", font=5, command=lambda: play(r.get()))
Play.pack(side=LEFT, padx=10, pady=20)
Exit1.pack(pady=20)

# Execute tkinter
root.mainloop()
