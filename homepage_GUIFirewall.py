# from idlelib.tooltip import Hovertip
import subprocess
import sys
from tkinter import *

from tkinter_custom_button import *

# functions end

des = Tk()
des.title("Home Page")
des.maxsize(width=1050, height=500)
des.minsize(width=1050, height=500)
# des.iconbitmap('icon.jpg')


des.title("MalSmart Dashboard")


def spawn_program_and_die(program, exit_code=0):
    # Start the external program
    subprocess.Popen(program)
    # We have started the program, and can suspend this interpreter
    sys.exit(exit_code)


def donothing():
   filewin = Toplevel(des)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def newProgramOpen():
    spawn_program_and_die(['python', 'loginGUI.py'])

menubar = Menu(des)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Close & New", command=newProgramOpen)
# filemenu.add_command(label="Open", command=donothing)
# filemenu.add_command(label="Save", command=donothing)
# filemenu.add_command(label="Save as...", command=donothing)
# filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=des.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
# editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

# editmenu.add_command(label="Cut", command=donothing)
# editmenu.add_command(label="Copy", command=donothing)
# editmenu.add_command(label="Paste", command=donothing)
# editmenu.add_command(label="Delete", command=donothing)
# editmenu.add_command(label="Select All", command=donothing)

# menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

des.config(menu=menubar)


#canvas = Canvas(des, width = 20, height = 20)
#canvas.pack()
#img = ImageTk.PhotoImage(Image.open("settingsimage.png"))
#canvas.create_image(20, 20, anchor=NW, image=img)





label_0 = Label(des, text="You have basic protection",width=20,font=("bold", 20))
label_0.place(x=370,y=23)
label_0.configure(foreground="green")


# img = ImageTk.PhotoImage()


# create label and add resize image
# label1 = Label(image=img)
# label1.image = img
# label1.pack()
# label1.place(x=350,y=23)

# label_1 = Label(des, text="Basic protection",width=20,font=(10))
# label_1.place(x=140,y=120)

# label_2 = Label(des, text="Full protection",width=40,font=( 10))
# label_2.place(x=600,y=120)

# Label Name Start
# Label Name End
# Entry Box Start
# Entry Box End

# frame



### onClick functions 

def payementsButtonOnClick():
    pass

def privacyButtonOnClick():
    pass

def webButtonOnClick():
    pass
def scanButtonOnClick():
    pass


###

## Images

#payementsImage = PhotoImage(file="paymentimage.png")
#payementsImage= payementsImage.zoom(100)   #25 signifies 250 pixels
#payementsImage= payementsImage.subsample(100)   #32 signifies 320 pixels
##

# Button Start

 

# Payments = Button(des, text="Payments", font='Verdana 13 bold', width=12, height=8)
# Payments.place(x=990, y=170)


payementsCustomButton = TkinterCustomButton(master=des,command=payementsButtonOnClick,text='Payments',width=150,height=150).place(x=750,y=170)



privacyCustomButton = TkinterCustomButton(master=des,command=privacyButtonOnClick,text='Privacy',width=150,height=150).place(x=450,y=170)


# hackerCustomButton = TkinterCustomButton(master=des,command=hackerButtonOnClick,text='Hacker',width=530,height=150).place(x=760,y=170)
# Hacker = Button(des, text="Hacker Attacks", font='Verdana 13 bold', width=12, height=8)
# Hacker.place(x=530, y=170)

webCustomButton = TkinterCustomButton(master=des,command=webButtonOnClick,text='Web and Email',width=150,height=150).place(x=150,y=170)


#comp = Button(des, text="Computer", font='Verdana 13 bold', width=12, height=8)
#comp.place(x=70, y=170)


scanCustomButton = TkinterCustomButton(master=des,command=webButtonOnClick,text='Scan',width=150,height=50).place(x=449,y=410)


des.mainloop()