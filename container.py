from tkinter import * 
import tkinter as tk
from ventas import Ventas
from inventario import Inventario
from clientes import Clientes
from pedidos import Pedidos
from proveedor import Proveedor
from informacion import Informacion
import sys
import os

class Container(tk.Frame):
    def __init__(self,padre,controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.configure(bg="white")
        self.pack()
        self.place(x=0,y=0,width=1100,height=650)
        self.widgets()
        self.frames = {}
        self.buttons = []

        for i in (Ventas, Inventario, Clientes, Pedidos, Proveedor, Informacion):
            frame = i(self)
            self.frames[i] = frame
            frame.pack()
            frame.config(bg="#C6D3E3", highlightbackground="gray", highlightthickness=1)
            frame.place(x=0,y=40,width=1100,height=610)
        self.show_frame(Ventas)

    def show_frame(self,container):
        frame = self.frames[container]
        frame.tkraise()

    def ventas(self):
        self.show_frame(Ventas)

    def inventario(self):
        self.show_frame(Inventario)
    
    def clientes(self):
        self.show_frame(Clientes)
    
    def pedidos(self):
        self.show_frame(Pedidos)

    def proveedor(self):
        self.show_frame(Proveedor)

    def informacion(self):
        self.show_frame(Informacion)
    
    def widgets(self):
        frame2 = Frame(self, bg="black")
        frame2.place(x=0, y=0, width=1100, height=40)

        # Lista de botones con sus propiedades
        botones = [
            {"text": "Ventas", "command": self.ventas},
            {"text": "Inventario", "command": self.inventario},
            {"text": "Clientes", "command": self.clientes},
            {"text": "Pedidos", "command": self.pedidos},
            {"text": "Proveedor", "command": self.proveedor},
            {"text": "Informacion", "command": self.informacion},
        ]

        # Crear botones dinámicamente
        for i, boton in enumerate(botones):
            frame = Frame(frame2, bg="black")
            frame.place(x=i * 184, y=0, width=184, height=40)
            btn = Button(frame, text=boton["text"], command=boton["command"], bg="white", font=("Arial", 12))
            btn.place(x=0, y=0, width=184, height=40)

            
