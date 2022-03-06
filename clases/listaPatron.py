from tkinter import commondialog
from .nodoPatron import nodoPatron

from dis import code_info


class listaPatron:
    
    def __init__(self):
        self.inicio = self.fin = None

    #Devuelve True si la lista esta vacia, False en caso contrario
    def estaVacia(self):
        return self.inicio == None

    def push(self, codigo, valor):
        if self.inicio == None:
            #Inicializando la pila
            self.fin = self.inicio = nodoPatron(None, codigo, valor)
        else:
            
            #agregando el valor al (inicio) de la lista
            ultimo = nodoPatron(None,codigo , valor)
            self.fin.siguiente = ultimo
            self.fin = ultimo

    def imprimir(self):
        temp = self.inicio
        while  temp != None:
            print(temp.codigo)
            temp = temp.siguiente
    

    def buscar(self,codigo):
        temp = self.inicio
        while  temp != None:
            if temp.codigo == codigo:
                return temp.valor

            temp = temp.siguiente
            

    
