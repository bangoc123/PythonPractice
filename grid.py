from Tkinter import *

import tkMessageBox

names = ["Ngoc", "Giang", "Hoang"]


def login(username_input,password_input):

    username="ngoc"

    password="123"

    count = 0

    if username == username_input:
        if password == password_input:

            root = Tk()

            root.wm_title("Application")

            menu = Menu(root)

            root.config(menu=menu)

            subMenu = Menu(menu)

            menu.add_cascade(label="File", menu = subMenu)

            subMenu.add_command(label="Now Project...")

            # frame = Frame(root, width=600, heigh=500)
            root.mainloop()

            # for name in names:
            #     label = Label(frame, text=name)
            #     label.pack()
            #
            # frame.pack(fill=X)



        else:
            tkMessageBox.showinfo("Notice", "Wrong password")
    else:
        tkMessageBox.showinfo("Notice", "Wrong Username")







root = Tk()

root.wm_title()

root.wm_title("Training X Team")

frame = Frame(root, width=100, height=30, bg='#ed1561')

nameLabel = Label(frame, text="Username:", padx=100, pady=20, justify=LEFT, bg='#ed1561', fg='white')

nameInput = Entry(frame)

nameLabel.pack(side=LEFT)

nameInput.pack(side=LEFT, padx=30)




frame2 = Frame(root, width=100, bg='#0076da')

passwordLabel = Label(frame2, text="Password:", padx=100, pady=20,  justify=LEFT,bg='#0076da', fg='white')

passwordInput = Entry(frame2)

passwordInput.insert(0, 'password...')

passwordLabel.pack(side=LEFT)

passwordInput.pack(side=LEFT,padx=30)


def loginView():
    # tkMessageBox.showinfo('Successful', 'Successful')

    name = nameInput.get().strip().lower()

    password = passwordInput.get().strip().lower()

    print name

    print password

    login(username_input=name, password_input=password)




    '''
    login()

    root = Tk()

    root.wm_title(name)

    root.mainloop()
    '''

button = Button(root,text="Submit", command=loginView)

frame.pack(fill=X)

frame2.pack(fill=X)

button.pack()

root.mainloop()




