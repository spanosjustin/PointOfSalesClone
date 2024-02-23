# Ring up guests
from datetime import datetime
from tkinter import *
from menuDisplay import *
import sys

# set up the GUI
master = Tk()
master.title("IPOS Clone")
canvas_width = 600
canvas_height = 600

w = Canvas(master, width=canvas_width, height=canvas_height, bg="#000000")

w.pack()

# Initializing Data
running = True

# Get and format the currewnt date and time
now = datetime.now()
dateAndTime = now.strftime("%d/%m/%y, %H:%M")

# variables

# display screen
def display():

    ## number buttons
    def managerClicked(*args):
        displayMenuScreen(w)

    #### NUMERICAL BUTTONS
    ## zero
    w.create_rectangle(0, 60, 80, 110, outline="#36373b", fill="#36373b", tag="menuButton")
    w.create_text(40, 85, text="MENU", font=("Helvetica", 20), tags="menuButton")

    ## number utility
    w.tag_bind("menuButton","<Button-1>",managerClicked)

# Calls the display function
display()
