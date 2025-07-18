# import tkinter library,using alias tk
import tkinter as tk

# initiate main window using Tk() method
root = tk.Tk()

# define window size
root.geometry("640x480") 

# define window title
root.title("First GUI by Monalisha")

# add a label
label = tk.Label(root, text="Hello world!", font=('Calibri', 18))
label.pack(padx=20, pady=20)
label1 = tk.Label(root,text="This is my first GUI",font=('Arial', 16))
label1.pack()
label3 = tk.Label(root, text="I am starting from the basics of tkinter", font=('Arial', 16))
label3.pack()

# generate text box
textbox = tk.Text(root, height=4, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

# generate the button
button = tk.Button(root, text="Click Here!", font=('Arial', 18))
button.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=("Arial", 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)


btn2 = tk.Button(buttonframe, text="2", font=("Arial", 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=("Arial", 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=("Arial", 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=("Arial", 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=("Arial", 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

#
anotherbutton = tk.Button(root, text="TEST")
anotherbutton.place(x= 150, y=150, height=50, width=50)



# loop the window across the screen
root.mainloop()





