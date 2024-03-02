# a repository of all icons for the menu display
from tkinter import PhotoImage

# the library
def load_images():
    images = {
        'burger': PhotoImage(file='menu_icons/burger.png').subsample(18, 18),
        'soda': PhotoImage(file='menu_icons/soda.png').subsample(18, 18),
        'fries': PhotoImage(file='menu_icons/french-fries.png').subsample(18, 18),
        'meal': PhotoImage(file='menu_icons/meal.png').subsample(18, 18),
        'coffee': PhotoImage(file='menu_icons/coffee.png').subsample(18, 18),
        'milkshake': PhotoImage(file='menu_icons/milkshake.png').subsample(18, 18),
        'nuggets': PhotoImage(file='menu_icons/nuggets.png').subsample(18, 18),
        'taco': PhotoImage(file='menu_icons/taco.png').subsample(18, 18),
        'tea': PhotoImage(file='menu_icons/tea.png').subsample(18, 18)
    }
    return images
