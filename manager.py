from tkinter import *
from tkinter import ttk
from container import Container
from login import Login
from login import Registro
import sys
import os

class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Supermercado el vuelto loco")
        self.geometry("1100x650+120+20")
        self.resizable(False, False)

        container = Frame(self)
        container.pack(fill=BOTH, expand=True)
        container.configure(bg="black")

        self.frames = {} 
        for F in (Login, Registro, Container):
            frame = F(container, self)
            self.frames[F] = frame

        self.show_frame(Login)

        self.style = ttk.Style()
        self.style.theme_use("classic")
        self.style.configure("TButton", font=("Arial", 12))

    def show_frame(self, container):
        frame = self.frames[container] 
        frame.tkraise()

def main():
    app = Manager()
    app.mainloop()

if __name__ == "__main__":
    main()
