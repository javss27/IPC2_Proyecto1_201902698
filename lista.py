from nodo import Nodo

class ListaSimple:
    
    def _init_(self):
        self.inicio = self.fin = None

    #Devuelve True si la lista esta vacia, False en caso contrario
    def estaVacia(self):
        return self.inicio == None

    def push(self, nombrePiso, codigoPatron1, codigoPatron2,R,C,F,S, patron1, patron2):
        if self.estaVacia():
            #Inicializando la pila
            self.fin = self.inicio = Nodo(None,  nombrePiso, codigoPatron1, codigoPatron2,R,C,F,S, patron1, patron2)
        else:
            #agregando el valor al (inicio) de la lista
            self.fin = Nodo(self.fin, nombrePiso, codigoPatron1, codigoPatron2,R,C,F,S, patron1, patron2)