from tkinter import *
import tkinter as tk


class Pedidos(tk.Frame):
    def __init__(self,padre):
        super().__init__(padre)
        self.widgets()

    def widgets(self):
        label= Label(self, text="Pedidos", font=("Arial", 20), bg="#C6D3E3")
        label.pack()