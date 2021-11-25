import tkinter as tk
from tkinter import *
from pyqtgraph import configfile

root = Tk()
S = tk.Scrollbar(root)
root.geometry("1050x500")
T = tk.Text(root, height=4, width=500)
root.title("Results")
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set,foreground="red")
with open("Malicious_log.txt", 'r') as f:
    T.insert(tk.END, f.read())

# quote = """HAMLET: To be, or not to be--that is the question:
# Whether 'tis nobler in the mind to suffer
# The slings and arrows of outrageous fortune
# Or to take arms against a sea of troubles
# And by opposing end them. To die, to sleep--
# No more--and by a sleep to say we end
# The heartache, and the thousand natural shocks
# That flesh is heir to. 'Tis a consummation
# Devoutly to be wished."""
# T.insert(tk.END, quote)
tk.mainloop()