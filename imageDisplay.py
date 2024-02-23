# a repository of all icons for the menu display
from tkinter import PhotoImage

# the library
def load_images():
    images = {
        'burger': PhotoImage(file='menu_icons/burger.png'),
        'soda': PhotoImage(file='menu_icons/soda.png'),
        'fries': PhotoImage(file='menu_icons/french-fries.png'),
        'meal': PhotoImage(file='menu_icons/meal.png'),
    }
    return images
