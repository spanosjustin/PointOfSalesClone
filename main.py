# Ring up guests
from datetime import datetime
from tkinter import *
from menuDisplay import *
import sys

# set up the GUI
master = Tk()
master.title("IPOS Clone")
canvas_width = 800
canvas_height = 600

w = Canvas(master, width=canvas_width, height=canvas_height, bg="#000000")

w.pack()

# Initializing Data
running = True

# Get and format the currewnt date and time
now = datetime.now()
dateAndTime = now.strftime("%d/%m/%y, %H:%M")

# variables

### METHODS AND FUNCTIONS

# display screen
def display():
    ## System functions methods
    def menuTabClicked(*args):
        displayMenuScreen(w)
        
    def funcButton(*args):
       displayFuncScreen(w)

    def managerButton(*args):
       displayManagerFunction(w)

    #### SYSTEM BUTTONS
    ## menu button
    w.create_rectangle(0, 60, 80, 110, outline="#36373b", fill="#36373b", tag="menuButton")
    w.create_text(40, 85, text="MENU", font=("Helvetica", 20), tags="menuButton")
    ## other functions
    w.create_rectangle(0, 115, 80, 165, outline="#36373b", fill="#36373b", tag="funcButton")
    w.create_text(40, 138, text="FUNC", font=("Helvetica", 20), tags="funcButton")
    ## manaer functions
    w.create_rectangle(0, 170, 80, 220, outline="#36373b", fill="#36373b", tag="managerButton")
    w.create_text(40, 192, text="MNGR", font=("Helvetica", 20), tags="managerButton")

    ## button pushed
    w.tag_bind("menuButton","<Button-1>",menuTabClicked)
    w.tag_bind("funcButton","<Button-1>",funcButton)
    w.tag_bind("managerButton","<Button-1>",managerButton)

    # display boarders
    boarderDisplay(w)

# Calls the display function
display()
