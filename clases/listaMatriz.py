from .nodoMatriz import nodoMatriz


class ListaSimple:
    
    def __init__(self):
        self.inicio = self.fin = None

    #Devuelve True si la lista esta vacia, False en caso contrario
    def estaVacia(self):
        return self.inicio == None

    def push(self, x, y , valor):
        if self.inicio == None:
            #Inicializando la pila
            self.fin = self.inicio = nodoMatriz(None, x, y , valor)
        else:
            
            #agregando el valor al (inicio) de la lista
            ultimo = nodoMatriz(None, x, y , valor)
            self.fin.siguiente = ultimo
            self.fin = ultimo

    

