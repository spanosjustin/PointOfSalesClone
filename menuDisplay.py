# menuDisplay.py
from tkinter import NW
import imageDisplay  # Import the module where images are loaded

def boarderDisplay(w):
    # banner
    w.create_rectangle(0, 0, 825, 25, outline="#36373b", fill="#36373b")
    # footer
    w.create_rectangle(0, 575, 825, 625, outline="#36373b", fill="#36373b")
    
### DISPLAYS
# Menu Display
def displayMenuScreen(w):
    images = imageDisplay.load_images()  # Load images
    # order window
    w.create_rectangle(500, 0, 750, 600, outline="#36373b", fill="white")
    # menu display
    w.create_rectangle(50, 0, 500, 800, outline="#7E7E7E", fill="#AAAAAA")
    w.create_image(50, 50, anchor=NW, image=images['burger'])
    boarderDisplay(w)

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
