# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Austin Biehl,8.10.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
# row - a single row in ToDoList.txt
strData = ''   # A row of text data from the file
dicRow = {}    # A row of data containing Task and Priority
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ''   # A menu of user options
strChoice = '' # A Capture the user option selection
strTask = ''    # The task to add or delete
strPriority =''      # The priority of the task being added
#
# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt","r")
for row in objFile:
    strData = row.split(",")
    dicRow = {"Task": strData[0], "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()
#
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new task.
    3) Remove an existing task.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input('Which option would you like to perform? [1 to 5]: '))
    # Step 3 - Show the current items in the table
    print() # Adding a new line for looks
    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print(dicRow)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = str(input('What task do you want to add?: '))
        strPriority = str(input('What priority should it have?: '))
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strTask = str(input('What task do you want to remove?: '))
        for row in lstTable:
            if row["Task"].lower() == strTask.lower():
                lstTable.remove(row)
                print(strTask, " was removed from your list")
            else:
                print('Task was not found in your list. Please check your spelling')
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open('ToDoList.txt', 'w')
        for dicRow in lstTable:
            objFile.write(dicRow['Task'] + ',' + dicRow['Priority'] + '\n')
        objFile.close()
        print('Your tasks were saved!')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Program Finished - Goodbye!')
        break                   # and Exit the program
    else:
        print('Please select a number between 1-5')