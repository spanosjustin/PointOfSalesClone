# menuDisplay.py
from tkinter import NW
import imageDisplay  # Import the module where images are loaded

def displayMenuScreen(w):
    images = imageDisplay.load_images()  # Load images
    # order window
    w.create_rectangle(500, 0, 750, 600, outline="#36373b", fill="white")
    # menu display
    w.create_image(50, 50, anchor=NW, image=images['burger'])
