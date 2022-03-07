from tkinter import Y
from clases import lista
from lector import iniciarAnalisis




# Array con las opciones del menu
menu_options = {
    1: "Cargar Archivo xml.",
    2: "Ver Pisos Disponibles.",
    3: "Ver Codigos.",
    4: "Salir de la aplicacion.",
}
# For que imprime las opciones del menu
def print_menu():
    print("\n")
    for key in menu_options.keys():
        print(key, "--", menu_options[key])
    print("\n")

# Metodo main el cual tiene un ciclo while para imprimir el menu
if __name__ == "__main__":
    while True:
        print_menu()
        option = ""
        try:
            option = int(input("Ingrese un numero: "))
        except:
            print("Entrada incorrecta. Por favor ingrese un numero ...")
        if option == 1:
            print("Iniciando Analisis....")
            global listaMenu 
            listaMenu =  iniciarAnalisis()
            print("Se han cargado los datos :D")
          
        elif option == 2:
            print("Pisos Disponibles")
            listaMenu.imprimir()
            option2 = input("Escriba el nombre del piso que desea ver: ")
            global verPiso
            verPiso = listaMenu.buscar(option2)
            print("Su piso a sido seleccionado. ")
        elif option == 3:
            verPiso.limpiar()
            print("Seleccionar codigo uno")
            
            verPiso.listaPatrones.imprimir()
            option2 = input("Escriba el nombre del primer codigo: ")
            patron = verPiso.listaPatrones.buscar(option2)
            verPiso.matrizUno.llenar(int(verPiso.R), int(verPiso.C),patron)
            verPiso.imprimirMatrizUno()
            print("Seleccionar codigo dos:")
            
            verPiso.listaPatrones.imprimir()
            option2 = input("Escriba el nombre del segundo codigo: ")   
            patron = verPiso.listaPatrones.buscar(option2)
            verPiso.matrizDos.llenar(int(verPiso.R), int(verPiso.C),patron)
            verPiso.imprimirMatrizDos()
            print("Pasos para cambiar el patron: ")
            print("1--Ver en consola: ")
            print("2--Generar en imgen: ")
            try:
                option = int(input("Ingrese un numero: "))
            except:
                print("Entrada incorrecta. Por favor ingrese un numero ...")
            if option == 1:
                print("Precio Total:", verPiso.calcular(True))
            if option == 2:
                print("Precio Total:", verPiso.calcular(False))
                verPiso.crearPasos()
        elif option == 4:
            print("Saliendo...")
            exit()
        else:
            print("Opcion invalida. Por favor ingresar un numero entre 1 y 5.")