# 3.5 from tkinter import *
from Tkinter import *
root = Tk() #create new window
root.wm_title("Training X Team")

label = Label(root,text="username")

label.pack()

nameInput = Entry(root)

nameInput.pack()
name = "Ngoc"
password = "123"
def login():
    if nameInput.get() == name:
        print "Successfully"

button = Button(root, text="Log in", command=login)

button.pack()

login()

root.mainloop()