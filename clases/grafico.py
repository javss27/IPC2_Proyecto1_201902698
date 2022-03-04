import os


def crearGrafico(dot, nombre):
    path = os.getcwd() + "/graficos/" + nombre + ".dot"
    
    # Abriendo el archivo en modo de escritura
    file = open(path, "w")
    file.write(dot)
    file.close()