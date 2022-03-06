


class nodoPatron:
    def __init__(self, siguiente,codigo,valor ):
        self.setSiguiente(siguiente)
        self.setValor( codigo,valor) 

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente
        
    def setValor(self, codigo ,valor):
        self.codigo= codigo 
        self.valor = valor


