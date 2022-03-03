from re import X


class nodoMatriz:
    def __init__(self, siguiente,x,y,valor ):
        self.setSiguiente(siguiente)
        self.setValor( x,y,valor) 

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def setValor(self,x,y,valor):
        self.x = x 
        self.y = y 
        self.valor = valor

    def getSiguiente(self):
        return self.siguiente

    def getValor(self):
        return self.valor