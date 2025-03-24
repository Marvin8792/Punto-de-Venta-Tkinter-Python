# Proyecto Python

Este proyecto utiliza varias librerías de Python para su funcionamiento. Asegúrate de instalarlas antes de ejecutar el código.

Requisitos

Necesitas tener Python instalado en tu sistema. Se recomienda usar un entorno virtual para gestionar las dependencias.

**Instalación de Dependencias**

Ejecuta los siguientes comandos para instalar las librerías necesarias:

```sh
pip install mysql-connector-python
```
```sh
pip install ttkthemes
```
```sh
pip install pillow
```
```sh
pip install tkcalendar
```
```sh
pip install reportlab
```


Usando un Entorno Virtual (Opcional)

Si deseas utilizar un entorno virtual, sigue estos pasos:

# Crear un entorno virtual
```sh
python -m venv venv
```

# Activar el entorno virtual
# En Windows
```sh
venv\Scripts\activate
```
# En macOS/Linux
```sh
source venv/bin/activate
```

# Instalar las dependencias dentro del entorno virtual
```sh
pip install -r requirements.txt
```
Archivo de Requisitos

Para facilitar la instalación en otros entornos, puedes guardar las dependencias en un archivo requirements.txt ejecutando:

pip freeze > requirements.txt

Y luego instalar todo con:

```sh
pip install -r requirements.txt
```

Uso

Después de instalar las dependencias, ejecuta el programa con:

```sh
python index.py
```

Contacto

Si tienes preguntas o sugerencias, no dudes en contribuir o ponerte en contacto con el equipo de desarrollo.