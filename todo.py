
import tkinter as tk
import tkinter.font as font


def deleteTask(taskList):
    # clear the entry box widget
    entryBox.delete(0, tk.END)
    # clear tasklist container
    taskList.clear()

    # clear widgets from the scrollable frame
    for w in scrollable_frame.grid_slaves():
        if isinstance(w, tk.Label) or isinstance(w, tk.Checkbutton):
            w.destroy()
    
    # Update scrollregion
    canvas.configure(scrollregion=canvas.bbox("all"))

# Bind mousewheel to canvas scrolling
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def addTask():
    value = entryBox.get()
    taskList.append(value)

    for i in range(len(taskList)):
        taskLabel = tk.Label(scrollable_frame, text=f"{i+1}."+ taskList[i])
        taskLabel.grid(row=1+i, column=0)

        checkBox = tk.Checkbutton(scrollable_frame)
        checkBox.grid(row=1+i, column=1)

        # Update scrollregion
    canvas.configure(scrollregion=canvas.bbox("all"))




window = tk.Tk()
window.title("Welcome to To-Do list")
window.geometry("660x480")

taskList =[]
entry_font = font.Font(family="Monospace", size=16)  # or try Helvetica, Courier New, etc.


entryBox = tk.Entry(window, width=48,font=entry_font)
entryBox.grid(row=0, column=0, ipady=2, padx=10, pady=10)

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

canvas = tk.Canvas(window, width=66 * 7, height=34 * 20)
scrollBar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.grid(row=1, column=0, columnspan=2)
scrollBar.grid(row=1,column=2, sticky="ns")

canvas.configure(yscrollcommand=scrollBar.set)

# Create a frame inside the canvas to hold widgets
scrollable_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")


canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))   # Linux scroll down
canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # Linux scroll up

# Scroll handling
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_configure)



window.mainloop()
