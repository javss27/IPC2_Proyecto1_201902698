from lector import iniciarAnalisis




# Array con las opciones del menu
menu_options = {
    1: "Cargar Archivo xml.",
    2: "",
    3: "",
    4: "",
    5: "",
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
            iniciarAnalisis()
           
        elif option == 2:
            print("Cargando Instrucciones...")
        elif option == 3:
            print("Analizando...")
            
        elif option == 4:
            print("Generando reporte....")
            
        elif option == 5:
            print("Saliendo...")
            exit()
        else:
            print("Opcion invalida. Por favor ingresar un numero entre 1 y 5.")