from tkinter import *
import tkinter
import sqlite3
# import tkinter as tk
# import awesometkinter as atk
# from idlelib.tooltip import Hovertip
# from tkinter import messagebox
from tkinter import messagebox as ms
import re
import subprocess
import sys

from PIL import ImageTk
from PIL import Image

from tkinter_custom_button import *


# it works!
def signupButtonOnClick():
    pass
def loginButtonOnClick():
    pass

root = Tk()
root.geometry('500x500')
root.title("Registration Form")


label_0 = Label(root, text="Login MalSmart",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Email",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Password",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,show="*")
entry_2.place(x=240,y=180)

# Read the Image
image = Image.open("securityimage.jpeg")

# Resize the image using resize() method
resize_image = image.resize((150, 150))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()
label1.place(x=185,y=220)



def on_RegisterButtonClick():
    spawn_program_and_die(['python', 'registrationGUI.py'])


def spawn_program_and_die(program, exit_code=0):
    # Start the external program
    subprocess.Popen(program)
    # We have started the program, and can suspend this interpreter
    sys.exit(exit_code)

# spawn_program_and_die(['python', 'path/to/my/script.py'])

# # Or, as in OP's example
# spawn_program_and_die(['python', 'file2.py'])





def login():
    con = sqlite3.connect('users_final2.db') # connect to the database

    cur = con.cursor() # define a cursor
    #Find user If there is any take proper action
    find_user = ('SELECT * FROM USERS WHERE email = ? and password = ?')
    cur.execute(find_user,[(entry_1.get()),(entry_2.get())])
    results = cur.fetchall() # fetch all the found entries 
    if results:
        spawn_program_and_die(['python','home.py'])
    else:
        ms.showerror('Oops!','Email or Password is Wrong.')

    





# spawn_program_and_die(['python', 'path/to/my/script.py'])

# # Or, as in OP's example
# spawn_program_and_die(['python', 'file2.py'])





# Button(root, text='Submit',width=20,bg='brown',fg='white',command=login).place(x=180,y=380)
loginButtonCustom = TkinterCustomButton(master=root,text='Login',command=login).place(x=200,y=380)

signupButtonCustom = TkinterCustomButton(master=root,text='Register',command=on_RegisterButtonClick).place(x=200,y=435)

# it is use for display the registration form on the window






root.mainloop()
print("registration form  seccussfully created...")