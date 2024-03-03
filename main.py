# Ring up guests
from datetime import datetime
from tkinter import *
#from menuDisplay import *
import imageDisplay
import random
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
# Extract the year, month, and day
year = now.year
month = now.month
day = now.day
# Format these components into a single integer (YYYYMMDD)
todays_date_int = int(f"{year}{month:02d}{day:02d}")

# variables
currentOrder = []
storeID = 1
daily_order_count = 0
orderID = None

def order_ID_generator():
    global daily_order_count
    global storeID
    global todays_date_int
    global orderID
    daily_order_count += 1
    random_number = random.randint(10, 99)
    orderID = int(f"{year}{month:02d}{day:02d}{storeID}{random_number}{daily_order_count}")
    print(orderID)
    return orderID
    

def boarderDisplay(w):
    # banner
    w.create_rectangle(0, 0, 825, 25, outline="#36373b", fill="#36373b")
    # footer
    w.create_rectangle(0, 575, 825, 625, outline="#36373b", fill="#36373b")

# Functions
def burgerButtonClicked(*args):
    print("Burger added to order")

def tacoButtonClicked(*args):
    print("Taco added to order")

def nuggetsButtonClicked(*args):
    print("Nuggets added to order")

### DISPLAYS
# Drinks display
def drinksDisplay(w):
    print("Displaying drinks")

# Menu Display
def displayMenuScreen(w):
    # generate order ID
    order_ID_generator()
    # set up the images
    global images
    images = imageDisplay.load_images()  # Load images
    burger_img = images['burger']
    taco_img = images['taco']
    nuggets_img = images['nuggets']
    # order window
    w.create_rectangle(500, 0, 750, 600, outline="#36373b", fill="white")
    # Order ID display
    w.create_text(545, 40, text="Order ID: ", font=("Helvetica", 14), fill="blue")
    w.create_text(660, 40, text=orderID, font=("Helvetica", 14), fill="blue")
    # directionary ques
    w.create_text(515, 55, text="#", font=("Helvetica", 16), fill="blue")
    w.create_text(560, 55, text="$.$$", font=("Helvetica", 16), fill="blue")
    w.create_text(680, 55, text="product", font=("Helvetica", 16), fill="blue")
    # sub total
    w.create_rectangle(500, 530, 750, 535, outline="#36373b", fill="white")
    w.create_text(550, 550, text="Subtotal:", font=("Helvetica", 20), fill="red")
    ### MENU DISPLAY
    # burger
    w.create_rectangle(125, 70, 175, 120, outline="#7E7E7E", fill="#AAAAAA", tags="burgerButton")
    w.create_image(135, 75, anchor=NW, image=burger_img)
    w.create_text(150, 110, text="Burgr", font=("Helvetica", 14), fill="#C23A00")
    boarderDisplay(w)
    # taco
    w.create_rectangle(185, 70, 235, 120, outline="#7E7E7E", fill="#AAAAAA", tags="tacoButton")
    w.create_image(195, 75, anchor=NW, image=taco_img)
    w.create_text(210, 110, text="Taco", font=("Helvetica", 14), fill="#C23A00")
    boarderDisplay(w)
    # nuggets
    w.create_rectangle(245, 70, 295, 120, outline="#7E7E7E", fill="#AAAAAA", tags="nuggetsButton")
    w.create_image(255, 75, anchor=NW, image=nuggets_img)
    w.create_text(270, 110, text="Nugts", font=("Helvetica", 14), fill="#C23A00")
    boarderDisplay(w)

    ## button pushed
    w.tag_bind("burgerButton","<Button-1>",burgerButtonClicked)
    w.tag_bind("tacoButton","<Button-1>",tacoButtonClicked)
    w.tag_bind("nuggetsButton","<Button-1>",nuggetsButtonClicked)

# Other FRunction Display
def displayFuncScreen(w):
    # order window
    w.create_rectangle(500, 0, 750, 600, outline="#36373b", fill="grey")
    boarderDisplay(w)

# Manager Function Display
def displayManagerFunction(w):
    print("Manager Function")
    boarderDisplay(w)

# remove displays
def removeDisplay(w, display):
    w.delete(display)

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
master.mainloop()
