class Nodo:
    def __init__(self, siguiente, nombrePiso, codigoPatron1, codigoPatron2,R,C,F,S, patron1, patron2):
        self.setSiguiente(siguiente)
        self.setValor( nombrePiso, codigoPatron1, codigoPatron2, R,C,F,S, patron1, patron2)

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def setValor(self, nombrePiso,codigoPatron1, codigoPatron2, R,C,F,S, patron1, patron2):
        self.nombrePiso = nombrePiso
        self.codigoPatron1 = codigoPatron1
        self.codigoPatron2 = codigoPatron2
        self.R = R
        self.C = C
        self.F = F
        self.S = S
        self.patron1 = patron1
        self.patron2 = patron2

    def getSiguiente(self):
        return self.siguiente

    def getValor(self):
        return self.valor