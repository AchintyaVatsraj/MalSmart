
from idlelib.tooltip import Hovertip
from tkinter_custom_button import *     #use this for the table
from tkinter import *
import sqlite3
import tkinter as tk
# import awesometkinter as atk
import idlelib.tooltip
from tkinter import messagebox 
from tkinter import messagebox as ms
import re
import subprocess
import sys

# from PIL import ImageTk
# from PIL import Image

### Database Code

con = sqlite3.connect('users_final2.db')

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS USERS(
    USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    fname text NOT NULL,
    email text UNIQUE NOT NULL,
    password text NOT NULL,
    gender text NOT NULL,
    age INTEGER NOT NULL
)
''')

con.commit() # add the table if not already existing.
###


root = Tk()
root.geometry('480x500')
root.title("MalSmart Personal Security Suite")

# footer = tk.Frame(root, bg='white', height=30,text="This is a  test text")
# footer.pack(fill='both', side='bottom')

#button_1 = TkinterCustomButton(master=root,text="My Button", corner_radius=10, command=button_function)
#button_1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#button_1.place(x=250,y=280)
def spawn_program_and_die(program, exit_code=0):
    # Start the external program
    subprocess.Popen(program)
    # We have started the program, and can suspend this interpreter
    sys.exit(exit_code)
def on_RegisterButtonClick():
    spawn_program_and_die(['python', 'registrationGUI.py'])

def loginButtOnClick():
    spawn_program_and_die(['python', 'loginGUI.py'])

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53) 


label_1 = Label(root, text="Full  Name:",width=20,font=("bold", 10))
label_1.place(x=80,y=130)



fullname_entry = Entry(root)
fullname_entry.place(x=240,y=130)

label_2 = Label(root, text="Email:",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

email_entry = Entry(root)
email_entry.place(x=240,y=180)

label_3 = Label(root, text="Gender:",width=20,font=("bold", 10)) 
label_3.place(x=70,y=280)
gender_entry = Entry(root)
gender_entry.place(x=240,y=280)
var = IntVar()


label_4 = Label(root, text="Age:",width=20,font=("bold", 10))
label_4.place(x=70,y=330)
age_entry = Entry(root)
age_entry.place(x=240,y=330)


label_5 = Label(root,text="Password:",width=20,font=("bold",10))
label_5.place(x=70,y=230) 
password_entry = Entry(root,show="*")
password_entry.place(x=240,y=230) 


genderTip = Hovertip(gender_entry,'Please Enter "Male" OR "Female".')
fnameTip = Hovertip(fullname_entry,'Please enter your Name here!')
ageTip = Hovertip(age_entry,'You must be above 18 years of age.')
emailTip = Hovertip(email_entry,'Please enter a vaild email!')
passwordTip = Hovertip(password_entry,'Below are the rules for Password:\n1. At least 8 Characters.\n2. At least one small letter.\n3. At least one Captial letter.\n4. At least one special character.\n5. At least one number.')

# def warning():
#     mb.showerror("OK","Please Enter Male or Female ONLY.")


# if age_entry.get() == "Male" or age_entry.get() == "Female":
#     pass
# else:
#     # diaglogBox with an OK Button , and when the button is clicked the age field will be clered.
#     age_entry.delete(0, 'end')
#     messagebox.showwarning("Warning","Warning message")

re_email = re.findall('\S+@\S+', email_entry.get()) # match the email and output a list
pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.in')
matches= pattern.findall(email_entry.get())




def submitButtonClick():
    if gender_entry.get() == "Male" or gender_entry.get() == "Female":
        pass
    else:
        # diaglogBox with an OK Button , and when the button is clicked the age field will be clered.
        gender_entry.delete(0, 'end')
        messagebox.showwarning("Warning","Please Enter Male or Female in Gender.")

    if int(age_entry.get()) >= 18:
        pass
    else:
        # diaglogBox with an OK Button , and when the button is clicked the age field will be clered.
        age_entry.delete(0, 'end')
        messagebox.showwarning("Warning","Please be an adult.")

    cur.execute("INSERT INTO USERS (fname,email,password,gender,age) VALUES(?,?,?,?,?)",(fullname_entry.get(),email_entry.get(),password_entry.get(),gender_entry.get(),age_entry.get()))
    # Commit your changes in the database
    con.commit()
    messagebox.showinfo("Alert!","User Registered!") # newly added

    # Closing the connection
    con.close()
 
    # if re_email == []:
    #     email_entry.delete(0,'end')
    #     messagebox.showwarning("Warning","Please enter a vaild email.")
    # else:
    #     pass

    
    


# button object calling a functions on Click
#button = tk.Button(root, text='Submit',width=20,bg='brown',fg='white',command=submitButtonClick).place(x=180,y=380)

submitButtonCustom = TkinterCustomButton(master=root,text='Register',command=submitButtonClick).place(x=180,y=380)
# atk.tooltip(button,"Click to register with us!")
loginButtonCustom = TkinterCustomButton(master=root,text='Login',command=loginButtOnClick).place(x=180,y=440)

# button.bind('<Button-1>', hello) # no need not removing will see later

# # Insert part of the sqlite3 database , keeping commented until we are able to store all the data from different entries!

#cur.execute("INSERT INTO USERS (fname,email,gender,age) VALUES(?,?,?,?)",(fullname_entry.get(),email_entry.get(),gender_entry.get(),age_entry.get()))

# con.close()
# cur.execute('''INSERT INTO USERS (fname,email,gender,age) VALUES (
#     ''
# )
# ''')








root.mainloop()
print("registration form  seccussfully created...") # testing messege will remove later!




###

# 1. change the name of all text Fileds to meningfull ones.
# 2. add comments to atrribues where possibles 

#vijetha hi!
###