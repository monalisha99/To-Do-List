
import tkinter as tk
import tkinter.font as font


def addTask(event=None):
    entry_box_value = entryBox.get()
    entry_box_value = entry_box_value.strip()

    if len(entry_box_value) == 0:
        entryBox.insert(0, 'Enter Task Here ..')

    if (entry_box_value != 'Enter Task Here ..') and len(entry_box_value)!=0:
        # Store tasks to taskList
        taskList.append(entry_box_value)

    if entry_box_value == 'Enter Task Here ..':
        # clear the entry box widget
        entryBox.delete(0, tk.END)

    if (len(entry_box_value)!=0) and (entry_box_value is not None) or (len(taskList)!=0):
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

# Define an empty list to store tasks entered
taskList =[]

# # Read tasks.text file
# try:
#     with open("tasks.txt", "r") as file:
#         for line in file:
#             # store tasks in taskList
#             # line = line.strip()
#             print(line)
#             taskList.append(line)

#         addTask()
# except:
#     print('No file found')

with open("tasks.txt", "r") as file:
    for line in file:
        # store tasks in taskList
        # line = line.strip()
        print(line)
        taskList.append(line)

    


# Designing the User Interface
window = tk.Tk()
window.title("Welcome to To-Do list")
window.geometry("760x480")


entry_font = font.Font(family="Monospace", size=16)

entryBox = tk.Entry(window, width=48,font=entry_font)
entryBox.grid(row=0, column=0, ipady=2, padx=10, pady=10)

# Define save button and place it
saveButton = tk.Button(window, text="Save", font=("Arial,11"), command=saveTasks)
saveButton.grid(row=0, column=3,ipady=5, padx=10, sticky="e")

addButton = tk.Button(window, 
                      text="Add",
                      font=('Arial',11),
                      bg='#89CFF0',
                      fg='black', 
                      activebackground='blue', 
                      activeforeground='white', 
                      command=lambda:addTask())
addButton.grid(row=0, column=1, padx=3, ipady=5)

deleteButton = tk.Button(window, 
                         text="Delete",
                         font=('Arial',11),
                         bg="#FA5C51",
                         fg='white', 
                         activebackground="#BA0D01", 
                         activeforeground='white', 
                         command=lambda:deleteTask(taskList))
deleteButton.grid(row=0, column=2, padx=3, ipady=5)

canvas = tk.Canvas(window, width=550, height=34 * 20)
scrollBar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.grid(row=1, column=0, columnspan=2)
scrollBar.grid(row=1,column=2, sticky="ns")

canvas.configure(yscrollcommand=scrollBar.set)

# Create a frame inside the canvas to hold widgets
scrollableFrame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollableFrame, anchor="nw")

addTask()


canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))   # Linux scroll down
canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # Linux scroll up

# Bind the Enter key to the addTask() function
entryBox.bind("<Return>", addTask)

window.mainloop()
