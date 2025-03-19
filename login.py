from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk 

class Login(tk.Frame):
    def __init__(self,padre, controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0,y=0,width=1100,height=650)
        self.config(bg="#C6D3E3")
        self.controlador = controlador
        self.widgets()

    def widgets(self):

        fondo = tk.Frame(self, bg="#C6D3E3")
        fondo.pack()
        fondo.place(x=0, y=0, width=1100, height=650)

        self.bg_imagen = Image.open("imagenes/supermarket.jpg")
        self.bg_imagen = self.bg_imagen.resize((1100, 650))
        self.bg_imagen = ImageTk.PhotoImage(self.bg_imagen)
        self.bg_label = Label(fondo, image=self.bg_imagen)
        self.bg_label.place(x=0, y=0, width=1100, height=650)
        
        #Frame blanco para el login
        frame1 = tk.Frame(self, bg="#ffffff", highlightbackground="black", highlightthickness=2)
        frame1.place(x=550, y=50, width=400, height=560)

        #Label para Nombre de usuario
        user = Label(frame1, text="Nombre de Usuario", font=("Arial", 16, "bold"), background="#ffffff")
        user.place(x=50, y=260)
        self.username = Entry(frame1, font=("Arial", 14), width=20)
        self.username.place(x=50, y=300, width=300, height=35)

        #Label para Contraseña
        password = Label(frame1,text="Contraseña", font=("Arial", 16, "bold"), background="#ffffff")
        password.place(x=50, y=340)
        self.password = Entry(frame1,font=("Arial", 14), width=20, show="*")
        self.password.place(x=50, y=380, width=300, height=35)
        
        #Boton de Iniciar Sesion
        self.boton = Button(frame1, text="Iniciar Sesion", font=("Arial", 14), bg="#1C1C1C", fg="#ffffff")
        self.boton.place(x=50, y=450, width=300, height=40)

        #Boton de Registro
        self.boton = Button(frame1, text="Registrarse", font=("Arial", 14), bg="#1C1C1C", fg="#ffffff")
        self.boton.place(x=50, y=500, width=300, height=40)
       

class Registro(tk.Frame):
    def __init__(self,padre, controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0,y=0,width=1100,height=650)
        self.controlador = controlador
        self.widgets()

    def widgets(self):
        fondo = tk.Frame(self, bg="#C6D3E3")
        fondo.pack()
        fondo.place(x=0, y=0, width=1100, height=650)

        self.bg_imagen = Image.open("imagenes/supermarket.jpg")
        self.bg_imagen = self.bg_imagen.resize((1100, 650))
        self.bg_imagen = ImageTk.PhotoImage(self.bg_imagen)
        self.bg_label = Label(fondo, image=self.bg_imagen)
        self.bg_label.place(x=0, y=0, width=1100, height=650)
        
        #Frame blanco para el login
        frame1 = tk.Frame(self, bg="#ffffff", highlightbackground="black", highlightthickness=2)
        frame1.place(x=550, y=10, width=400, height=600)

        #Label para Nombre de usuario
        user = Label(frame1, text="Nombre de Usuario", font=("Arial", 16, "bold"), background="#ffffff")
        user.place(x=50, y=260)
        self.username = Entry(frame1, font=("Arial", 14), width=20)
        self.username.place(x=50, y=300, width=300, height=35)

        #Label para Contraseña
        password = Label(frame1,text="Contraseña", font=("Arial", 16, "bold"), background="#ffffff")
        password.place(x=50, y=340)
        self.password = Entry(frame1,font=("Arial", 14), width=20, show="*")
        self.password.place(x=50, y=380, width=300, height=35)

        key = Label(frame1,text="Clave", font=("Arial", 16, "bold"), background="#ffffff")
        key.place(x=50, y=420)
        self.key = Entry(frame1,font=("Arial", 14), width=20, show="*")
        self.key.place(x=50, y=460, width=300, height=35)
        
        #Boton de Iniciar Sesion
        self.boton = Button(frame1, text="Registrarse", font=("Arial", 14), bg="#1C1C1C", fg="#ffffff")
        self.boton.place(x=50, y=510, width=300, height=40)