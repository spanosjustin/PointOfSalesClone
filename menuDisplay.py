# menuDisplay.py
from tkinter import NW
import imageDisplay  # Import the module where images are loaded

def displayMenuScreen(w):
    images = imageDisplay.load_images()  # Load images
    print("Displaying Menu Screen")
    # Example of displaying an image, adjust coordinates as needed
    w.create_image(50, 50, anchor=NW, image=images['burger'])
