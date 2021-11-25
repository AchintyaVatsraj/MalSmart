from tkinter import*
from tkinter.ttk import Treeview

from PIL import ImageTk,Image


class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('Action', 'From', 'status')
        tv.heading("#0", text='To', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('Action', text='Start Time')
        tv.column('Action', anchor='center', width=100)
        tv.heading('From', text='End Time')
        tv.column('From', anchor='center', width=100)

        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        var = IntVar()
        Radiobutton( text="+", padx=5, variable=var, value=1).place(x=10, y=100)
        Radiobutton( text="-", padx=20, variable=var, value=2).place(x=50, y=100)


    def LoadTable(self):
        self.treeview.insert('', 'end', text="51413/tcp", values=('ALLOW IN',
                             'Anywhere'))
        self.treeview.insert('', 'end', text="51413/udp", values=('ALLOW IN',
                                                              'Anywhere'))

def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()