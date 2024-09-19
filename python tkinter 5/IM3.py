from tkinter import *  

root = Tk()
root.geometry("400x300")
root.title("Main Window")

def topwin():
    top = Toplevel() 
    top.geometry("180x180")
    top.title("Toplevel Window")

    l2 = Label(top, text="This is a Toplevel window")
    l2.pack()

# Main window widgets
l1 = Label(root, text="This is the root window")
btn = Button(root, text="Click here to open another window", command=topwin)

# Packing the widgets
l1.pack()
btn.pack()

root.mainloop()
