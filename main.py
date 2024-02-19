# Clock in and track work hours
from datetime import datetime
from tkinter import *
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
shiftHour = 0
shiftMinute = 0
totalShift = 0
weeklyHoursWorked = 0.00
userNumInput = []
utilityHeight = canvas_height / 5

# Intitializing Data Base
employeeData = {
    123456: {
        "name": "Justin Spanos",
        "isClockedIn": False,
        "Hourly Rate": 17.75
        },
    654321: {
        "name": "Natalia Spanos",
        "isClockedIn": False,
        "Hourly Rate": 18.00
        },
    111111: {
        "name": "Yo Momma",
        "isClockedIn": False,
        "Hourly Rate": 15.70
        }
    }

# For Later
employeeWorkWeekData = {
    123456: {
        "in":{},
        "out":{},
        "shifts":{},
        "total hours":{},
        },
    654321: {
        "in":{},
        "out":{},
        "shifts":{},
        "total hours":{},
        },
    111111: {
        "in":{},
        "out":{},
        "shifts":{},
        "total hours":{},
        }
    }

managerNumbers = [123456]

# Functions
# loads data from a .txt file
##try:
##    with open("employeeWorkWeekData.txt", "r") as file:
##        employeeData = str(file.read())
##except FileNotFoundError:
##    print("No data")
##
### save function
##def saveData():
##    with open("employeeWorkWeekData.txt", "w") as file:
##        file.write(str(employeeWorkWeekData))

# turns string input into an integer
def listToInt(myInput):
    myString = ''.join(myInput)
    newInputNumber = int(myString)
    return newInputNumber    

# Calculates length of shift
def shiftLength():
    print("entered function")
    global employeeInUse
    global employeeWorkWeekData
    global shiftMinute
    global shiftHour
    # Variables
    clockInTime = str(employeeWorkWeekData[employeeInUse]["in"])
    clockOutTime = str(employeeWorkWeekData[employeeInUse]["out"])
    
    clockInHour = int(clockInTime[14:16])
    clockInMin = int(clockInTime[17:19])
    clockOutHour = int(clockOutTime[14:16])
    clockOutMin = int(clockOutTime[17:19])
    
    # Logic for hours
    if(clockOutHour >= clockInHour):
        shiftHour = clockOutHour - clockInHour
    else:
        clockOutHour += 24
        shiftHour = clockOutHour - clockInHour
    # Logic for minutes
    if(clockOutMin >= clockInMin):
        shiftMinute = clockOutMin - clockInMin
    else:
        clockOutMin += 60
        shiftMinute = clockOutMin - clockInMin
    # Combine Minutes and hours
    shiftMinute = round((shiftMinute / 60), 2)
    totalShift = shiftHour + shiftMinute
    for x in range(len(employeeWorkWeekData[employeeInUse]["shifts"]) + 1):
        if(x >= len(employeeWorkWeekData[employeeInUse]["shifts"])):
            employeeWorkWeekData[employeeInUse]["shifts"][x] = totalShift
            employeeWorkWeekData[employeeInUse]["shifts"][x]
    print(employeeWorkWeekData[employeeInUse]["shifts"][len(employeeWorkWeekData[employeeInUse]["shifts"])-1])

#
##
# Will repurpose this into checking the length of user input
##
#

def functioning():
    employeeInUse = int(input("Enter Numbers: "))

    # Check if number is the correct length
    if(employeeInUse < 6 and employeeInUse > 6 and employeeInUse != -1):
        invalidFunction()
    # Check if the number is the correct number
    if(employeeInUse != -1 and employeeData[employeeInUse]["isClockedIn"] == False):
        clockIn()
            
    elif(employeeInUse != -1 and employeeData[employeeInUse]["isClockedIn"] == True):
        clockOut()
        
    elif(employeeInUse == -1):
        totalWeeklyHours()

# display screen
def display():

    newInputNumber = 0

    # variables
    displayNum = w.create_text(canvas_width / 2, canvas_height / 5, text=newInputNumber, tag="display_num", font=("Helvetica", 26), anchor="center")
    displayText = None
    validInputLen = False

    def managerDisplay(windowInUse):
        global employeeData
        global employeeWorkWeekData
        global shiftMinute
        global shiftHour
        global utilityHeight
        tempHeight = utilityHeight / 5
        # Display Manager Information
        for x in employeeWorkWeekData.keys():
            windowInUse.create_text((canvas_width / 4), tempHeight, text="Employee Name: {} \nEmployee ID: {}".format(employeeData[x]["name"], x), tag="display_num", font=("Helvetica", 18), anchor="center")
            tempHeight = tempHeight + 80
            windowInUse.create_text((canvas_width / 2), tempHeight, text="Times: \nIn: {}\nOut: {}\nShifts: {}\nTotal Hours: {}".format(employeeWorkWeekData[x]["in"], employeeWorkWeekData[x]["out"], employeeWorkWeekData[x]["shifts"],employeeWorkWeekData[x]["total hours"]), tag="display_num", font=("Helvetica", 18), anchor="center")
            tempHeight = tempHeight + 80

    def managerAccess():
        nonlocal newInputNumber
        for x in range(len(managerNumbers)):
            if(newInputNumber == managerNumbers[x]):
                secondWindow = Tk()
                secondWindow.title("Manager Screen")
                managerWin = Canvas(secondWindow, width=canvas_width, height=canvas_height * (len(employeeWorkWeekData.keys()) / 3), bg="#000000")
                managerWin.pack()
                managerDisplay(managerWin)
        clearUserInput()

    # Prints invalid inputs
    def invalidFunction():
        nonlocal displayText
        nonlocal displayNum
        w.delete(displayText)
        w.delete(displayNum)
        displayNum = w.create_text(canvas_width / 2, utilityHeight, text="Invalid Input", tag="display_num", font=("Helvetica", 26), anchor="center")

    def checkInputLength(inputNum):
        if(inputNum < 6 and inputNum > 6):
            validInputLen == True
        return validInputLen

    def resetUserInput():
        nonlocal displayNum
        nonlocal newInputNumber
        userNumInput.clear()
        newInputNumber = 0
        return userNumInput, newInputNumber

    # Clears user input and resets it to zero
    def clearUserInput():
        # function variables
        nonlocal displayNum
        nonlocal newInputNumber
        nonlocal displayText
        # logic
        userNumInput.clear()
        newInputNumber = 0
        # update display
        w.delete(displayText)
        w.delete(displayNum)
        displayNum = w.create_text(canvas_width / 2, utilityHeight, text=newInputNumber, tag="display_num", font=("Helvetica", 26), anchor="center")
        return userNumInput, newInputNumber

    # Clock in function
    def clockIn():
        global employeeInUse
        global employeeData
        global employeeWorkWeekData
        nonlocal newInputNumber
        nonlocal displayNum
        nonlocal displayText
        # check length of input
        #checkInputLength(len(newInputNumber))
        # logic
        currentTime = datetime.now()
        timeIn = currentTime.strftime("%d/%m/%y %H:%M")
        if newInputNumber in employeeData:
            employeeData[newInputNumber]["isClockedIn"] = True
            w.delete(displayNum)
            displayText = w.create_text(canvas_width / 2, (utilityHeight/2) + 50, text="    Clocked In \n   {} \n {}".format(employeeData[newInputNumber]["name"], dateAndTime), tag="display_num", font=("Helvetica", 20), anchor="center")
            for x in range(len(employeeWorkWeekData[newInputNumber]["in"]) + 1):
                if(x >= len(employeeWorkWeekData[newInputNumber]["in"])):
                    employeeWorkWeekData[newInputNumber]["in"][x] = timeIn
        resetUserInput()
        w.delete(displayNum)

    # add up and calculate the total hours of the week
    def totalWeeklyHours():
        print("Entered totalWeeklyHours")
        global employeeInUse
        global employeeWorkWeekData
        global weeklyHoursWorked
        employeeCalc = int(input("Enter Employee Numbers: "))
        for x in range(len(employeeWorkWeekData[employeeCalc]["shifts"]) + 1):
            #if(x >= len(employeeWorkWeekData[employeeCalc]["shifts"])):
            print(employeeWorkWeekData[employeeCalc]["shifts"][x])
            print(weeklyHoursWorked)

    # Clock out function
    def clockOut():
        global employeeInUse
        global employeeData
        global employeeWorkWeekData
        nonlocal newInputNumber
        nonlocal displayNum
        nonlocal displayText
        currentTime = datetime.now()
        timeIn = currentTime.strftime("%d/%m/%y %H:%M")
        if newInputNumber in employeeData:
            employeeData[newInputNumber]["isClockedIn"] = False
            recentShift = len(employeeWorkWeekData[newInputNumber]["shifts"])
            w.delete(displayNum)
            displayText = w.create_text(canvas_width / 2, (utilityHeight/2) + 50, text="    Clocked Out \n  {} \n {} \n{}".format(employeeData[newInputNumber]["name"], dateAndTime, "Hours worked"), tag="display_num", font=("Helvetica", 20), anchor="center")
            for x in range(len(employeeWorkWeekData[newInputNumber]["out"]) + 1):
                if(x >= len(employeeWorkWeekData[newInputNumber]["out"])):
                    employeeWorkWeekData[newInputNumber]["out"][x] = timeIn
        totalWeeklyHours()
        resetUserInput()
        w.delete(displayNum)

    # Updates and displays user input in real time
    def buttonInputUpdate(num):
        # function variables
        nonlocal displayNum
        nonlocal newInputNumber
        # update variables
        userNumInput.append(num)
        newInputNumber = listToInt(userNumInput)
        # update display
        w.delete(displayText)
        w.delete(displayNum)
        displayNum = w.create_text(canvas_width / 2, canvas_height / 5, text=newInputNumber, tag="display_num", font=("Helvetica", 26), anchor="center")
    
    ## number buttons
    def managerClicked(*args):
        managerAccess()
        
    def zeroClicked(*args):
        buttonInputUpdate('0')

    def oneClicked(*args):
        buttonInputUpdate('1')

    def twoClicked(*args):
        buttonInputUpdate('2')

    def threeClicked(*args):
        buttonInputUpdate('3')

    def fourClicked(*args):
        buttonInputUpdate('4')

    def fiveClicked(*args):
        buttonInputUpdate('5')

    def sixClicked(*args):
        buttonInputUpdate('6')

    def sevenClicked(*args):
        buttonInputUpdate('7')

    def eightClicked(*args):
        buttonInputUpdate('8')

    def nineClicked(*args):
        buttonInputUpdate('9')

    # Function buttons
    def clockInClicked(*args):
        clockIn()
        
    def clockOutClicked(*args):
        clockOut()

    def clearClicked(*args):
        clearUserInput()
        
    
    #### NUMERICAL BUTTONS
    ## zero
    w.create_rectangle(185, 500, 415, 575, outline="#36373b", fill="#36373b", tag="zeroButton")
    w.create_text(300, 537, text="0", font=("Helvetica", 26), tags="zeroButton")
    
    ## one
    w.create_rectangle(185, 400, 245, 475, outline="#36373b", fill="#36373b", tag="oneButton")
    w.create_text(215, 437, text="1", font=("Helvetica", 26), tags="oneButton")
    ## two
    w.create_rectangle(270, 400, 330, 475, outline="#36373b", fill="#36373b", tag="twoButton")
    w.create_text(300, 437, text="2", font=("Helvetica", 26), tags="twoButton")
    ## three
    w.create_rectangle(355, 400, 415, 475, outline="#36373b", fill="#36373b", tag="threeButton")
    w.create_text(385, 437, text="3", font=("Helvetica", 26), tags="threeButton")

    ####
    ## four
    w.create_rectangle(185, 300, 245, 375, outline="#36373b", fill="#36373b", tag="fourButton")
    w.create_text(215, 337, text="4", font=("Helvetica", 26), tags="fourButton")
    ## five
    w.create_rectangle(270, 300, 330, 375, outline="#36373b", fill="#36373b", tag="fiveButton")
    w.create_text(300, 337, text="5", font=("Helvetica", 26), tags="fiveButton")
    ## six
    w.create_rectangle(355, 300, 415, 375, outline="#36373b", fill="#36373b", tag="sixButton")
    w.create_text(385, 337, text="6", font=("Helvetica", 26), tags="sixButton")
    
    
    ####
    ## seven
    w.create_rectangle(185, 200, 245, 275, outline="#36373b", fill="#36373b", tag="sevenButton")
    w.create_text(215, 237, text="7", font=("Helvetica", 26), tags="sevenButton")
    ## eight
    w.create_rectangle(270, 200, 330, 275, outline="#36373b", fill="#36373b", tag="eightButton")
    w.create_text(300, 237, text="8", font=("Helvetica", 26), tags="eightButton")
    ## nine
    w.create_rectangle(355, 200, 415, 275, outline="#36373b", fill="#36373b", tag="nineButton")
    w.create_text(385, 237, text="9", font=("Helvetica", 26), tags="nineButton")


    ####
    ## operational buttons
    # manager button
    w.create_rectangle(100, 350, 160, 425, outline="#36373b", fill="#36373b", tag="managerButton")
    w.create_text(130, 387, text="Mng", font=("Helvetica", 24), tags="managerButton")
    
    ## clock in
    w.create_rectangle(440, 450, 500, 525, outline="#36373b", fill="#36373b", tag="clockIn")
    w.create_text(470, 487, text="In", font=("Helvetica", 24), tags="clockIn")

    ## clock out
    w.create_rectangle(440, 350, 500, 425, outline="#36373b", fill="#36373b", tag="clockOut")
    w.create_text(470, 387, text="Out", font=("Helvetica", 24), tags="clockOut")
    
    ## clear
    w.create_rectangle(440, 250, 500, 325, outline="#36373b", fill="#36373b", tag="clearButton")
    w.create_text(470, 287, text="CLR", font=("Helvetica", 24), tags="clearButton")
    

    ## number utility
    w.tag_bind("zeroButton","<Button-1>",zeroClicked)
    
    w.tag_bind("oneButton","<Button-1>",oneClicked)
    w.tag_bind("twoButton","<Button-1>",twoClicked)
    w.tag_bind("threeButton","<Button-1>",threeClicked)
    
    w.tag_bind("fourButton","<Button-1>",fourClicked)
    w.tag_bind("fiveButton","<Button-1>",fiveClicked)
    w.tag_bind("sixButton","<Button-1>",sixClicked)
    
    w.tag_bind("sevenButton","<Button-1>",sevenClicked)
    w.tag_bind("eightButton","<Button-1>",eightClicked)
    w.tag_bind("nineButton","<Button-1>",nineClicked)

    w.tag_bind("managerButton","<Button-1>",managerClicked)
    w.tag_bind("clearButton","<Button-1>",clearClicked)
    w.tag_bind("clockOut","<Button-1>",clockOutClicked)
    w.tag_bind("clockIn","<Button-1>",clockInClicked)

# Calls the display function
display()
