from traceback import print_tb
from turtle import position
from wsgiref.validate import validator
from clases import lista
from .listaMatriz import ListaSimple


class matriz:
    def __init__(self):
        self.matriz = ListaSimple()

    def llenar(self,x,y, patron):
        posicion = 0
        for i in range(x):
            for j in range(y):
            
                self.matriz.push(i,j,patron[posicion])
                posicion += 1
    
    def buscar(self,x,y):
        temp = self.matriz.inicio
        
        while  temp != None:
            if temp.x == x and temp.y == y:
                return temp.valor
            temp = temp.siguiente

    def cambiar(self,x,y,valor):
        temp = self.matriz.inicio
        while  temp != None:
            if temp.x == x and temp.y == y:
                temp.valor = valor
                return
            temp = temp.siguiente

    def switch(self,x,y):
        temp = self.matriz.inicio
        while  temp != None:
            if temp.x == x and temp.y == y:
                if temp.valor == "W":
                    temp.valor = "B"
                elif temp.valor == "B":
                    temp.valor ="W"
                return 
            temp = temp.siguiente
