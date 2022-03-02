from .nodo import Nodo


class ListaSimple:
    
    def __init__(self):
        self.inicio = self.fin = None

    #Devuelve True si la lista esta vacia, False en caso contrario
    def estaVacia(self):
        return self.inicio == None

    def push(self, nombrePiso, codigoPatron1, codigoPatron2,R,C,F,S, patron1, patron2):
        if self.inicio == None:
            #Inicializando la pila
            self.fin = self.inicio = Nodo(None,  nombrePiso, codigoPatron1, codigoPatron2,R,C,F,S, patron1, patron2)
        else:
            
            #agregando el valor al (inicio) de la lista
            ultimo = Nodo(None, nombrePiso, codigoPatron1, codigoPatron2,R,C,F,S, patron1, patron2)
            self.fin.siguiente = ultimo
            self.fin = ultimo

    def imprimir(self):
        temp = self.inicio
        while  temp != None:
            print(temp.nombrePiso)
            print(temp.codigoPatron1)
            print(temp.R)
            temp = temp.siguiente

