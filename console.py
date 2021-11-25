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
                        "bg": "black",
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
        self.stop()
        thread = Thread(target=self._run, daemon=True, args=(command, ))
        thread.start()

    def _run(self, command:str) -> None:
        """
        Runs the command using subprocess and appends the output
        to `self.text_to_show`
        """
        self.proc = Popen(command, shell=True, stdout=PIPE)

        try:
            while self.proc.poll() is None:
                text = self.proc.stdout.read(1).decode()
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


if __name__ == "__main__":
    def run_command_in_entry(event:tk.Event=None):
        console.run(entry.get())
        entry.delete("0", "end")
        return "break"

    root = tk.Tk()
    root.title("Console")

    console = Console(root)
    console.pack(expand=True, fill="both")

    entry = tk.Entry(root, bg="black", fg="white",
                     insertbackground="white")
    entry.insert("end", "ping 8.8.8.8 -n 4")
    entry.bind("<Return>", run_command_in_entry)
    entry.pack(fill="x")

    root.mainloop()