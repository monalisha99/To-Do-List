import tkinter as tk
import tkinter.font as font

def on_select():
    print('Variable selected.', var.get())


root = tk.Tk()

root.title('To Do List')
root.geometry('640x480')

# variables
var = tk.StringVar(value="A")


# Add Widgets here, we will use .pack() method

entry_box_label = tk.Label(root, text="Enter Task: ", font=("courier", 18))
entry_box_label.grid(row=0, column=0)

entry_box = tk.Entry(root, width=60)
entry_box.grid(row=0, column=1)

radio_btn = tk.Radiobutton(root, padx=20, variable=var, value='A, command=on_select')
radio_btn.grid(row=0, column=2)

root.mainloop()
