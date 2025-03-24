from conexionbd import obtener_conexion
from tkinter import *
import tkinter as tk
from container import Container
from PIL import Image, ImageTk
from tkinter import messagebox

class Login(tk.Frame):

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0, y=0, width=1100, height=650)
        self.config(bg="#C6D3E3")
        self.controlador = controlador
        self.widgets()

    def validacion(self, user, pas):
        return len(user) > 0 and len(pas) > 0

    def login(self):
        user = self.username.get()
        pas = self.password.get()
        if self.validacion(user, pas):
            consulta = "SELECT * FROM usuarios WHERE usuario = %s AND password = %s"
            parametros = (user, pas)

            try:
                # Obtener la conexión desde conexionbd.py
                conn = obtener_conexion()
                if conn and conn.is_connected():
                    cursor = conn.cursor()
                    cursor.execute(consulta, parametros)
                    result = cursor.fetchone()

                    if result:
                        self.control1()
                    else:
                        self.username.delete(0, END)
                        self.password.delete(0, END)
                        messagebox.showerror(title="Error", message="Usuario y/o contraseña incorrectos")
            except Exception as e:
                messagebox.showerror(title="Error", message=f"Error en la conexión: {e}")
            finally:
                if conn and conn.is_connected():
                    conn.close()
        else:
            messagebox.showerror(title="Error", message="Llene todas las casillas")

    def control1(self):
        self.controlador.show_frame(Container)

    def control2(self):
        self.controlador.show_frame(Registro)

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

        self.image_regis = Image.open("imagenes/registro.png")
        self.image_regis = self.image_regis.resize((170, 170))
        self.image_regis = ImageTk.PhotoImage(self.image_regis)
        self.label = Label(frame1, image=self.image_regis, bg="#ffffff")
        self.label.place(x=100, y=30)

        #Label para Nombre de usuario
        user = Label(frame1, text="Nombre de Usuario", font=("Arial", 16, "bold"), background="#ffffff")
        user.place(x=50, y=220)
        self.username = Entry(frame1, font=("Arial", 14), width=20, bg="#B6E7F2")
        self.username.place(x=50, y=250, width=300, height=35)

        #Label para Contraseña
        password = Label(frame1,text="Contraseña", font=("Arial", 16, "bold"), background="#ffffff")
        password.place(x=50, y=300)
        self.password = Entry(frame1,font=("Arial", 14), width=20, show="*", bg="#FFD9D5")
        self.password.place(x=50, y=330, width=300, height=35)
        
        #Boton de Iniciar Sesion
        self.boton = Button(frame1, text="Iniciar Sesion", font=("Arial", 14, "bold"), bg="#6879E5", fg="Black", command=self.login)
        self.boton.place(x=50, y=390, width=300, height=40)

        #Boton de Registro
        self.boton = Button(frame1, text="Registrarse", font=("Arial", 14, "bold"), bg="#F29188", fg="Black", command=self.control2)
        self.boton.place(x=50, y=450, width=300, height=40)
       

class Registro(tk.Frame):
    def __init__(self,padre, controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0,y=0,width=1100,height=650)
        self.controlador = controlador
        self.widgets()

    def validacion(self, user, pas):
        return len(user) > 0 and len(pas) > 0

    def eje_consulta(self,consulta, parametros=()):
        try:
            conn = obtener_conexion()
            if conn and conn.is_connected():
                cursor = conn.cursor()
                cursor.execute(consulta, parametros)
                conn.commit()
        except Exception as e:
            messagebox.showerror(title="Error", message=f"Error en la conexión: {e}")

    def registro(self):
        user = self.username.get()
        pas = self.password.get()
        key = self.key.get()
        if self.validacion(user, pas):
            if len(pas) < 8:
                messagebox.showinfo(title="Error", message="La contraseña debe tener al menos 8 caracteres")
                self.username.delete(0, END)
                self.password.delete(0, END)
            else:
                if key == "1234":
                    consulta = "INSERT INTO usuarios VALUES (%s, %s, %s)"
                    parametros = (None, user, pas)
                    self.eje_consulta(consulta, parametros)
                    self.control1()
                else:
                    messagebox.showinfo(title="Error", message="Error al ingresar el codigo de registro")
        else:
            messagebox.showerror(title="Error", message="Llene todas las casillas")

    def control1(self):
        self.controlador.show_frame(Container)

    def control2(self):
        self.controlador.show_frame(Login)
    

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

        #Imagen de Registro
        self.image_regis = Image.open("imagenes/registro.png")
        self.image_regis = self.image_regis.resize((200, 200))
        self.image_regis = ImageTk.PhotoImage(self.image_regis)
        self.label = Label(frame1, image=self.image_regis, bg="#ffffff")
        self.label.place(x=100, y=30)

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
        
        #Boton de registro
        self.boton = Button(frame1, text="Registrarse", font=("Arial", 14), bg="#6879E5", fg="Black", command=self.registro)
        self.boton.place(x=50, y=510, width=300, height=40)

        self.boton = Button(frame1, text="Volver", font=("Arial", 14), bg="#F29188", fg="Black", command= self.control2)
        self.boton.place(x=150, y=555, width=100, height=30)