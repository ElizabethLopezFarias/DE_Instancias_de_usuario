import json

from usuario import Usuario  # importacion de la clase Usuario

usuarios = []  # Lista para almacenar las instancias de Usuario

try:
    #abre archivos usuarios.txt en modo lectura
    with open("usuarios.txt", "r") as archivo:
        for linea in archivo:  #itera sobre los elementos en archivo
            datos_usuario = json.loads(linea.strip())  # Interpreta la línea como JSON
            usuario = Usuario(
                nombre=datos_usuario["nombre"],
                apellido=datos_usuario["apellido"],
                email=datos_usuario["email"],
                genero=datos_usuario["genero"]
            )
            usuarios.append(usuario)
# manejo de excepción si no encuentra el archivo
except FileNotFoundError:
    print("El archivo usuarios.txt no se encuentra.")
# manejo de excepción de contenido del archivo
except json.JSONDecodeError:
    print("Error al interpretar el contenido como JSON.")

# Ahora la lista 'usuarios' contiene las instancias creadas
print(usuarios)
