from tkinter import*
from PIL import ImageTk,Image

import re
import subprocess
import sys

from tkinter_custom_button import TkinterCustomButton

root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("hacker.jpg"))
canvas.create_image(20, 50, anchor=NW, image=img)


root.geometry('500x500')
root.title("Firewall")

label_0 = Label(root, text="Firewall",width=20,font=("bold", 20))
label_0.place(x=90,y=23)



label_3 = Label(root, text="Status ",width=20,font=("bold", 10))
label_3.place(x=70,y=250)
var = IntVar()
Radiobutton(root, text="On",padx = 5, variable=var, value=1).place(x=235,y=250)
Radiobutton(root, text="Off",padx = 20, variable=var, value=2).place(x=290,y=250)
Button(root, text='Submit',width=10,bg='DodgerBlue3',fg='white').place(x=220,y=410)

def spawn_program_and_die(program, exit_code=0):
    # Start the external program
    subprocess.Popen(program)
    # We have started the program, and can suspend this interpreter
    sys.exit(exit_code)
def tableButtonClick():
    spawn_program_and_die(['python', 'addtable.py'])


submitButtonCustom = TkinterCustomButton(master=root,text='Add table',command=tableButtonClick).place(x=200,y=450)
#Button(root, text='Open Table',width=20,bg='brown',fg='white').place(x=180,y=410)



variable1 = StringVar(root)
variable1.set("Deny") # default value

label_4 = Label(root, text="Incoming: ",width=20,font=("bold", 10))
label_4.place(x=70,y=300)
label_4 = Label(root, text="Outgoing: ",width=20,font=("bold", 10))
label_4.place(x=70,y=350)

w = OptionMenu(root, variable1, "Allow", "Deny").place(x=235,y=300)


variable2 = StringVar(root)
variable2.set("Allow") # default value

v = OptionMenu(root, variable2, "Allow", "Deny").place(x=235,y=350)



root.mainloop()
print("registration form  seccussfully created...")
