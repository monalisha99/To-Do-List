
import tkinter as tk
import tkinter.font as font

# define a function as addTask and takes one optional argument: event
# event= None means,this function can be called with or without an event (e.g., a button click or pressing Enter in a GUI).
def addTask(event=None):
    # gets the user text from the entrybox 
    entry_box_value = entryBox.get() 
    # remove white spaces     
    entry_box_value = entry_box_value.strip()      

    # if entrybox is empty or no text
    if len(entry_box_value) == 0:
        # display texts as: Enter task Here
        entryBox.insert(0, 'Enter Task Here ..')

    # if entry box has not 'Enter task Here' and text is not 0
    if (entry_box_value != 'Enter Task Here ..') and len(entry_box_value)!=0:
        # Store tasks to taskList
        taskList.append(entry_box_value)

    # if the entrybox text exactly 'Enter Task Here''
    if entry_box_value == 'Enter Task Here ..':
        # clear the entry box widget
        entryBox.delete(0, tk.END)

    # if entrybox text not 0 and not null or tasklist is not 0,that means, only show tasks if input is valid or task list isn’t empty
    if (len(entry_box_value)!=0) and (entry_box_value is not None) or (len(taskList)!=0):
        # looping through taskList and display as labels
        for i in range(len(taskList)):
            taskLabel = tk.Label(scrollableFrame, text=f"{i+1}. "+ taskList[i], font=entry_font)
            taskLabel.grid(row=i, column=0, sticky='nw')

            checkBox = tk.Checkbutton(scrollableFrame, font=("Arial", 16))
            checkBox.grid(row=i, column=1, padx=5)

        # Update scrollregion
        canvas.configure(scrollregion=canvas.bbox("all"))
    
        # clear the entry box widget
        entryBox.delete(0, tk.END)


def deleteTask(taskList):
    # clear the entry box widget
    entryBox.delete(0, tk.END)
    # clear tasklist container
    taskList.clear()
    

    # clear widgets from the scrollable frame
    for w in scrollableFrame.grid_slaves():
        w.destroy()
    


# Bind mousewheel to canvas scrolling
def mouseWheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")


# save tasks function
def saveTasks():
    with open("tasks.txt","w") as file:
        for t in taskList:
            file.write(t + "\n")



# Define an empty list to store texts entered in the entrybox
taskList =[]

# Try to Read tasks.txt file 
try: 
    with open("tasks.txt", "r") as file:
        for line in file:
            # store line in taskList container
            taskList.append(line)

# if no file exist as tasks.txt then print()
except:       
    print('No file found')

# Designing the User Interface
# define tkinter window 
window = tk.Tk()

# add atitle to the window
window.title("Welcome to To-Do list")

# set size of the window
window.geometry("760x480")

# define a font style, we are using monospace
entry_font = font.Font(family="Monospace", size=16)

# define an entrybox widget, it accepts text input
entryBox = tk.Entry(window, width=48,font=entry_font)

# place the entrybox using .grid geometry
entryBox.grid(row=0, column=0, ipady=2, padx=10, pady=10)

# define add button, the objective of the button is to add texts or tasks
# using the function addTask
addButton = tk.Button(window, 
                      text="Add",
                      font=('Arial',11),
                      bg='#89CFF0',
                      fg='black', 
                      activebackground='blue', 
                      activeforeground='white', 
                      command=lambda:addTask())

# place the button in row 0, column 1
addButton.grid(row=0, column=1, padx=3, ipady=5)

# define delete button, theb objective of the button is to delete the stored tasks
# using the function deleteTask
deleteButton = tk.Button(window, 
                         text="Delete",
                         font=('Arial',11),
                         bg="#FA5C51",
                         fg='white', 
                         activebackground="#BA0D01", 
                         activeforeground='white', 
                         command=lambda:deleteTask(taskList))

# place the button in row 0, column 2
deleteButton.grid(row=0, column=2, padx=3, ipady=5)

# Define save button, the objective of the button is to save tasks 
# using saveTasks function
saveButton = tk.Button(window, text="Save", font=("Arial,11"), command=saveTasks)

# place the button in row 0, column 3
saveButton.grid(row=0, column=3,ipady=5, padx=10, sticky="e")

canvas = tk.Canvas(window, width=550, height=34 * 20)
scrollBar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.grid(row=1, column=0, columnspan=2)
scrollBar.grid(row=1,column=2, sticky="ns")

canvas.configure(yscrollcommand=scrollBar.set)

# Create a frame inside the canvas to hold widgets
scrollableFrame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollableFrame, anchor="nw")

# Run this function once at app start to display existing tasks if any
addTask()


canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))   # Linux scroll down
canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # Linux scroll up

# Bind the Enter key to the addTask() function
entryBox.bind("<Return>", addTask)

window.mainloop()
