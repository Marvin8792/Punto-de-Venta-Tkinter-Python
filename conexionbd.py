import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        # Configuración de la conexión
        conn = mysql.connector.connect(
            host="localhost",       # Cambia esto por la dirección de tu servidor MySQL
            user="root",            # Tu usuario de MySQL
            password="root",        # Tu contraseña de MySQL
            database="basedatos"    # Nombre de tu base de datos
        )
        return conn
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None