from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus found")

# Create the button outside the function and correct the 'command' spelling
button = Button(root, text="Scan for virus", command=msg)
button.place(x=40, y=80)

root.mainloop()
