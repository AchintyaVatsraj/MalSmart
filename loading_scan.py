import subprocess
import time
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

# Create Tkinter Object
root = Tk()

root.geometry("1050x500")


frame1 = Frame(root,bg="white",width=500,height=300)



def update_progress_label():
    return f"Current Progress: {pb['value']}%"


def progress():
    if pb['value'] < 100:
        pb['value'] += 1
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='The progress completed!')


def stop():
    pb.stop()
    value_label['text'] = update_progress_label()

def spawn_program_and_die(program, exit_code=0):
    # Start the external program
    subprocess.Popen(program)
    # We have started the program, and can suspend this interpreter
    # sys.exit(exit_code)

def result():
    try:
        spawn_program_and_die(['python3', 'maliciousfiles.py'])
    except Exception as e:
        print(e)

s = ttk.Style()
s.theme_use("default")
s.configure("TProgressbar", thickness = 50)

pb = ttk.Progressbar(
    frame1,
    orient='horizontal',
    mode='determinate',
    length=1010,style = "TProgressbar"
)
pb.pack(ipady=10333)

pb.grid(column=0, row=0, columnspan=2, padx=10, pady=51)

# label
value_label = ttk.Label(frame1, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=2)

# start button
start_button = ttk.Button(
    frame1,
    text='Result',
    command=result
)
start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)



def load():
    for i in range(100):
        progress()
        time.sleep(2)
frame1.pack()

#
#
frame2 = Frame(root,bg="white",width=1000,height=1000)
from tkinter.scrolledtext import ScrolledText
from subprocess import Popen, PIPE
from threading import Thread, Lock
import tkinter as tk


class Console(ScrolledText):
    """
    Simple console that can execute commands
    """

    def __init__(self, master, **kwargs):
        # The default options:
        text_options = {"state": "disabled",
                        "bg": "white",
                        "fg": "#08c614",
                        "selectbackground": "orange"}
        # Take in to account the caller's specified options:
        text_options.update(kwargs)
        super().__init__(master, **text_options)

        self.proc = None # The process
        self.text_to_show = "" # The new text that we need to display on the screen
        self.text_to_show_lock = Lock() # A lock to make sure that it's thread safe

        self.show_text_loop()

    def clear(self) -> None:
        """
        Clears the Text widget
        """
        super().config(state="normal")
        super().delete("0.0", "end")
        super().config(state="disabled")

    def show_text_loop(self) -> None:
        """
        Inserts the new text into the `ScrolledText` wiget
        """
        new_text = ""
        # Get the new text that needs to be displayed
        with self.text_to_show_lock:
            new_text = self.text_to_show.replace("\r", "")
            self.text_to_show = ""

        if len(new_text) > 0:
            # Display the new text:
            super().config(state="normal")
            super().insert("end", new_text)
            super().see("end")
            super().config(state="disabled")

        # After 100ms call `show_text_loop` again
        super().after(100, self.show_text_loop)

    def run(self, command:str) -> None:
        """
        Runs the command specified
        """
        # self.stop()
        thread = Thread(target=self._run, daemon=True, args=("ls", ))
        thread.start()

    def _run(self, command:str) -> None:
        """
        Runs the command using subprocess and appends the output
        to `self.text_to_show`
        """
        self.proc = Popen(command, shell=True, stdout=PIPE,executable='/bin/bash')

        try:
            while self.proc.poll() is None:
                text = self.proc.stdout.read(1).decode('utf-8')
                with self.text_to_show_lock:
                    self.text_to_show += text

            self.proc = None
        except AttributeError:
            # The process ended prematurely
            pass

    def stop(self, event:tk.Event=None) -> None:
        """
        Stops the process.
        """
        try:
            self.proc.kill()
            self.proc = None
        except AttributeError:
            # No process was running
            pass

    def destroy(self) -> None:
        # Stop the process if the text widget is to be destroyed:
        self.stop()
        super().destroy()


# if __name__ == "__main__":
    # def run_command_in_entry(event:tk.Event=None):
def run_command_in_entry():
    # python3
    # scan.py
    thread0 = Thread(target=load)
    thread0.start()
    thread = Thread(target=console._run, daemon=True, args=("python3 scan.py",))
    thread.start()
    # thread.join()

    entry.delete("0", "end")
    return "break"

    # root = tk.Tk()
    # root.title("Console")

console = Console(frame2)
console.pack(expand=True, fill="both")

entry = tk.Entry(frame2, bg="black", fg="white",
                     insertbackground="white")
entry.insert("end", "python3 scan.py")
# entry.bind("<Return>", run_command_in_entry)
run_command_in_entry()
entry.pack(fill="x")

frame2.pack(pady=20,padx=20)

root.mainloop()



