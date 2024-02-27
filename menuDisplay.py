# menuDisplay.py
from tkinter import NW
import imageDisplay  # Import the module where images are loaded

def boarderDisplay(w):
    # banner
    w.create_rectangle(0, 0, 825, 25, outline="#36373b", fill="#36373b")
    # footer
    w.create_rectangle(0, 575, 825, 625, outline="#36373b", fill="#36373b")

# Functions
def burgerButtonClicked():
    print("Burger added to order")

def tacoButtonClicked():
    print("Taco added to order")

def nuggetsButtonClicked():
    print("Nuggets added to order")

### DISPLAYS
# Drinks display
def drinksDisplay(w):
    print("Displaying drinks")

# Menu Display
def displayMenuScreen(w):
    images = imageDisplay.load_images()  # Load images
    # order window
    w.create_rectangle(500, 0, 750, 600, outline="#36373b", fill="white")
    # directionary ques
    w.create_text(515, 40, text="#", font=("Helvetica", 16), fill="blue")
    w.create_text(560, 40, text="$.$$", font=("Helvetica", 16), fill="blue")
    w.create_text(680, 40, text="product", font=("Helvetica", 16), fill="blue")
    # sub total
    w.create_rectangle(500, 530, 750, 535, outline="#36373b", fill="white")
    w.create_text(550, 550, text="Subtotal:", font=("Helvetica", 20), fill="red")
    ### MENU DISPLAY
    # burger
    w.create_rectangle(125, 70, 175, 120, outline="#7E7E7E", fill="#AAAAAA", tags="burgerButton")
    w.create_image(50, 50, anchor=NW, image=images['burger'])
    w.create_text(150, 110, text="Burgr", font=("Helvetica", 14))
    boarderDisplay(w)
    # taco
    w.create_rectangle(185, 70, 235, 120, outline="#7E7E7E", fill="#AAAAAA", tags="tacoButton")
    w.create_image(50, 50, anchor=NW, image=images['burger'])
    w.create_text(210, 110, text="Taco", font=("Helvetica", 14))
    boarderDisplay(w)
    # nuggets
    w.create_rectangle(245, 70, 295, 120, outline="#7E7E7E", fill="#AAAAAA", tags="nuggetsButton")
    w.create_image(50, 50, anchor=NW, image=images['burger'])
    w.create_text(270, 110, text="Nugts", font=("Helvetica", 14))
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
