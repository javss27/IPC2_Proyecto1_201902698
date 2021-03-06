from .nodo import Nodo


class ListaSimple:
    
    def __init__(self):
        self.inicio = self.fin = None

    #Devuelve True si la lista esta vacia, False en caso contrario
    def estaVacia(self):
        return self.inicio == None

    def push(self,  nombrePiso, R,C,F,S, listaPatrones):
        if self.inicio == None:
            #Inicializando la pila
            self.fin = self.inicio = Nodo(None,   nombrePiso, R,C,F,S, listaPatrones)
        else:
            
            #agregando el valor al (inicio) de la lista
            ultimo = Nodo(None,  nombrePiso, R,C,F,S, listaPatrones)
            self.fin.siguiente = ultimo
            self.fin = ultimo

    def imprimir(self):
        temp = self.inicio
        while  temp != None:
            print(temp.nombrePiso)
            temp = temp.siguiente
    

    def buscar(self,nombre):
        temp = self.inicio
        while  temp != None:
            if temp.nombrePiso == nombre:
                return temp

            temp = temp.siguiente
            

    

