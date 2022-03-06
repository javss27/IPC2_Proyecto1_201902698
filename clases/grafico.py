import os


def guardarDot(dot, nombre):
    path = os.getcwd() + "/" + nombre + ".dot"
    
    # Abriendo el archivo en modo de escritura
    file = open(path, "w")
    file.write(dot)
    file.close()