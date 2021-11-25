# import time
# from tkinter import *
# from tkinter import ttk
# import tkinter as tk
# from tkinter.messagebox import showinfo
#
# # Create Tkinter Object
# root = Tk()
#
# root.geometry("1050x500")
#
#
# frame1 = Frame(root,bg="white",width=500,height=300)
#
#
#
# def update_progress_label():
#     return f"Current Progress: {pb['value']}%"
#
#
# def progress():
#     if pb['value'] < 100:
#         pb['value'] += 1
#         value_label['text'] = update_progress_label()
#     else:
#         showinfo(message='The progress completed!')
#
#
# def stop():
#     pb.stop()
#     value_label['text'] = update_progress_label()
#
# s = ttk.Style()
# s.theme_use("default")
# s.configure("TProgressbar", thickness = 50)
#
# pb = ttk.Progressbar(
#     frame1,
#     orient='horizontal',
#     mode='determinate',
#     length=1010,style = "TProgressbar"
# )
# pb.pack(ipady=10333)
#
# pb.grid(column=0, row=0, columnspan=2, padx=10, pady=51)
#
# # label
# value_label = ttk.Label(frame1, text=update_progress_label())
# value_label.grid(column=0, row=1, columnspan=2)
#
# # start button
# start_button = ttk.Button(
#     frame1,
#     text='Result',
#     command=progress
# )
# start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)
#
#
#
# def load():
#     for i in range(100):
#         progress()
#         time.sleep(2)
# frame1.pack()
#
# #
# #
# frame2 = Frame(root,bg="white",width=1000,height=1000)
# from tkinter.scrolledtext import ScrolledText
# from subprocess import Popen, PIPE
# from threading import Thread, Lock
# import tkinter as tk
#
#
# class Console(ScrolledText):
#     """
#     Simple console that can execute commands
#     """
#
#     def __init__(self, master, **kwargs):
#         # The default options:
#         text_options = {"state": "disabled",
#                         "bg": "black",
#                         "fg": "#08c614",
#                         "selectbackground": "orange"}
#         # Take in to account the caller's specified options:
#         text_options.update(kwargs)
#         super().__init__(master, **text_options)
#
#         self.proc = None # The process
#         self.text_to_show = "" # The new text that we need to display on the screen
#         self.text_to_show_lock = Lock() # A lock to make sure that it's thread safe
#
#         self.show_text_loop()
#
#     def clear(self) -> None:
#         """
#         Clears the Text widget
#         """
#         super().config(state="normal")
#         super().delete("0.0", "end")
#         super().config(state="disabled")
#
#     def show_text_loop(self) -> None:
#         """
#         Inserts the new text into the `ScrolledText` wiget
#         """
#         new_text = ""
#         # Get the new text that needs to be displayed
#         with self.text_to_show_lock:
#             new_text = self.text_to_show.replace("\r", "")
#             self.text_to_show = ""
#
#         if len(new_text) > 0:
#             # Display the new text:
#             super().config(state="normal")
#             super().insert("end", new_text)
#             super().see("end")
#             super().config(state="disabled")
#
#         # After 100ms call `show_text_loop` again
#         super().after(100, self.show_text_loop)
#
#     def run(self, command:str) -> None:
#         """
#         Runs the command specified
#         """
#         # self.stop()
#         thread = Thread(target=self._run, daemon=True, args=("ls", ))
#         thread.start()
#
#     def _run(self, command:str) -> None:
#         """
#         Runs the command using subprocess and appends the output
#         to `self.text_to_show`
#         """
#         self.proc = Popen(command, shell=True, stdout=PIPE,executable='/bin/bash')
#
#         try:
#             while self.proc.poll() is None:
#                 text = self.proc.stdout.read(1).decode('utf-8')
#                 with self.text_to_show_lock:
#                     self.text_to_show += text
#
#             self.proc = None
#         except AttributeError:
#             # The process ended prematurely
#             pass
#
#     def stop(self, event:tk.Event=None) -> None:
#         """
#         Stops the process.
#         """
#         try:
#             self.proc.kill()
#             self.proc = None
#         except AttributeError:
#             # No process was running
#             pass
#
#     def destroy(self) -> None:
#         # Stop the process if the text widget is to be destroyed:
#         self.stop()
#         super().destroy()
#
#
# # if __name__ == "__main__":
#     # def run_command_in_entry(event:tk.Event=None):
# def run_command_in_entry():
#     # python3
#     # scan.py
#     thread0 = Thread(target=load)
#     thread0.start()
#     thread = Thread(target=console._run, daemon=True, args=("python3 scan.py",))
#     thread.start()
#     entry.delete("0", "end")
#     return "break"
#
#     # root = tk.Tk()
#     # root.title("Console")
#
# console = Console(frame2)
# console.pack(expand=True, fill="both")
#
# entry = tk.Entry(frame2, bg="black", fg="white",
#                      insertbackground="white")
# entry.insert("end", "python3 scan.py")
# # entry.bind("<Return>", run_command_in_entry)
# run_command_in_entry()
# entry.pack(fill="x")
#
# frame2.pack(pady=20,padx=20)
#
# root.mainloop()
#
#
#

# from tkinter import *
# import tkinter as tk
#
# root = Tk()
# Lb = Listbox(root)
# root.geometry("1050x500")
# Lb.grid()
# Lb.pack(padx=10,pady=10,expand=True)
# f = open("firewall_ports.txt","r")
# for x in f:
#     Lb.insert(END,x)
#     print(x)
# f.close()
#
# root.mainloop()

# from tkinter import*
# from tkinter.ttk import Treeview
#
# # from PIL import ImageTk,Image
#
#
# class App(Frame):
#
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#         self.CreateUI()
#         self.LoadTable()
#         self.grid(sticky = (N,S,W,E))
#         parent.grid_rowconfigure(0, weight = 1)
#         parent.grid_columnconfigure(0, weight = 1)
#
#     def CreateUI(self):
#         tv = Treeview(self)
#         tv['columns'] = ('Action', 'From', 'status')
#         tv.heading("#0", text='To', anchor='w')
#         tv.column("#0", anchor="w")
#         tv.heading('Action', text='Start Time')
#         tv.column('Action', anchor='center', width=100)
#         tv.heading('From', text='End Time')
#         tv.column('From', anchor='center', width=100)
#
#         tv.grid(sticky = (N,S,W,E))
#         self.treeview = tv
#         self.grid_rowconfigure(0, weight = 1)
#         self.grid_columnconfigure(0, weight = 1)
#
#         var = IntVar()
#         Radiobutton( text="+", padx=5, variable=var, value=1).place(x=10, y=100)
#         Radiobutton( text="-", padx=20, variable=var, value=2).place(x=50, y=100)
#
#
#     def LoadTable(self):
#         self.treeview.insert('', 'end', text="51413/tcp", values=('ALLOW IN',
#                              'Anywhere'))
#         self.treeview.insert('', 'end', text="51413/udp", values=('ALLOW IN',
#                                                               'Anywhere'))
#
# def main():
#     root = Tk()
#     App(root)
#     root.mainloop()
#
# if __name__ == '__main__':
#     main()
import os
from tkinter import ttk
import tkinter as tk
from tkinter import *

cmd = "./firewall.sh"
os.system(cmd)

my_w = tk.Tk()
my_w.geometry('1050x500')
my_w.title("FIREWALL")
trv = ttk.Treeview(my_w, selectmode='browse')
trv.grid(row=1, column=1, columnspan=4, padx=20, pady=20)
trv["columns"] = ("1","2", "3","4","5","6")
trv['show'] = 'headings'
trv.column("1", width=10, anchor='c')
trv.column("2", width=50, anchor='c')
trv.column("3", width=180, anchor='c')
trv.column("4", width=230, anchor='c')
trv.column("5", width=230, anchor='c')
trv.column("6", width=280, anchor='c')


# trv.heading("1", text="To")
trv.heading("2", text="S.no")
trv.heading("3", text="PORT")
trv.heading("4", text="ALLOW/DENY")
trv.heading("5", text="IN/OUT BOUND")
trv.heading("6", text="FROM")

i = 1
f = open("firewall_ports.txt","r")
for x in f:
    trv.insert("", 'end', text='', values=x)
    # trv.insert(END,x)
    print(x)
f.close()


l0 = tk.Label(my_w, text='Add entry',
              font=('Helvetica', 14), width=30, anchor="c")
l0.grid(row=2, column=1, columnspan=4)

l1 = tk.Label(my_w, text='PORT :', width=10, anchor="c")
l1.grid(row=3, column=1)

# add one text box
t1 = tk.Text(my_w, height=1, width=10, bg='white')
t1.grid(row=3, column=2)

l2 = tk.Label(my_w, text='Allow/Deny: ', width=10)
l2.grid(row=3, column=3)

# add list box for selection of class
options = StringVar(my_w)
options.set("")  # default value

opt1 = tk.Text(my_w, height=1, width=10, bg='white')
opt1.grid(row=3, column=4)

l3 = tk.Label(my_w, text='BOUND: ', width=10)
l3.grid(row=5, column=1)

# add one text box
t3 = tk.Text(my_w, height=1, width=10, bg='white')
t3.grid(row=5, column=2)

l4 = tk.Label(my_w, text='FROM: ', width=10)
l4.grid(row=5, column=3)

# add one text box
t4 = tk.Text(my_w, height=1, width=10, bg='white')
t4.grid(row=5, column=4)

l5 = tk.Label(my_w, text='DELETE ENTRY',
              font=('Helvetica', 14), width=30, anchor="c")
l5.grid(row=7, column=1, columnspan=4)

l6 = tk.Label(my_w, text='S.NO: ', width=10)
l6.grid(row=8, column=2)

# add one text box
t6 = tk.Text(my_w, height=1, width=10, bg='white')
t6.grid(row=8, column=3)

b1 = tk.Button(my_w, text='Add Record', width=10,
               command=lambda: add_data())
b1.grid(row=6, column=1)

b2 = tk.Button(my_w, text='Delete Record', width=10,
               command=lambda: del_data())
b2.grid(row=9, column=1)

b3 = tk.Button(my_w, text='Refresh', width=10,
               command=lambda: ref_data())
b3.grid(row=9, column=4)

my_str = tk.StringVar()
l5 = tk.Label(my_w, textvariable=my_str, width=10)
l5.grid(row=8, column=1)


def add_data():
    ad = opt1.get("1.0", END)
    port = t1.get("1.0", END)
    bound = t3.get("1.0", END)
    ad = ad.strip('\n')
    port = port.strip('\n')
    bound = bound.strip('\n')

    cmd="echo \"kali\" | sudo -S ufw "+ad+" "+bound+" "+port
    os.system(cmd)

def del_data():
    ad1 = t6.get("1.0", END)
    ad1 = ad1.strip('\n')
    cmd="echo \"y\" | sudo -S sudo ufw delete "+ ad1
    os.system(cmd)

def ref_data():
    ad1 = t6.get("1.0", END)
    ad1 = ad1.strip('\n')
    cmd="echo \"kali\" | sudo -S sudo ufw delete "+ ad1
    os.system(cmd)

my_w.mainloop()