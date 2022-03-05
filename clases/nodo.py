from .matriz import matriz
from .grafico import crearGrafico
from graphviz import render
from graphviz import Source
import os

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
        self.F = F #costo por volteo
        self.S = S #Costo por cambio
        self.patron1 = patron1.replace(" ","").replace("    ","").replace("\n","")
        self.patron2 = patron2.replace(" ","").replace("    ","").replace("\n","")
        
        self.matrizUno = matriz()
        self.matrizDos = matriz()
        self.matrizUno.llenar(int(R),int(C),self.patron1)
        self.matrizDos.llenar(int(R),int(C),self.patron2)
        self.precio = 0
        print(self.calcular())
        
    def calcular(self):
        completo = False
        while not completo:
            completo = True
            #for para las matrices
            for i in range(int(self.R)):
                
                for j in range(int(self.C)):
                    #Obteniendo posicion de azulejos 
                    azulejoUno = self.matrizUno.buscar(i,j)
                    azulejoDos = self.matrizDos.buscar(i,j)
                    
                    #realizando validaciones
                    if azulejoUno != azulejoDos:
                        #se espera que sean diferentes
                        #completo no esta completo 
                        completo = False
                        #buscando azulejo uno Abajo 
                        azulejoUnoAbajo = self.matrizUno.buscar(i+1,j)
                        azulejoDosAbajo = self.matrizDos.buscar(i+1,j)
                        azulejoUnoDerecha = self.matrizUno.buscar(i,j+1)
                        azulejoDosDerecha = self.matrizDos.buscar(i,j+1)
                        if int(self.F)*(2) > int(self.S):
                            
                            if  azulejoUnoAbajo != None:
                                if azulejoUnoAbajo == azulejoDos :
                                    if azulejoUnoAbajo != azulejoDosAbajo or (azulejoUnoAbajo == azulejoDosAbajo and int(self.F)*(2) > int(self.S)+int(self.F)):
                                #SI EL COSTO DE VOLTEO MAYOR A CAMBIO
                                    
                                        self.precio += int(self.S)
                                        #haciendo cambio de azulejos 
                                        self.matrizUno.cambiar(i+1,j,azulejoUno)
                                        self.matrizUno.cambiar(i,j, azulejoUnoAbajo)
                                        print("azulejo " , i,",",j, "intercambio abajo")
                                        print("Se intercambiaron azulejos :D")
                                        self.crearGrafico()
                                    else:
                                        self.voltearPiso(i,j)

                                elif  azulejoUnoDerecha != None:
                                    if azulejoUnoDerecha == azulejoDos:
                                        if azulejoUnoDerecha != azulejoDosDerecha or (azulejoUnoDerecha == azulejoDosDerecha and int(self.F)*(2) > int(self.S)+int(self.F)):
                                            self.precio += int(self.S)
                                            self.matrizUno.cambiar(i,j+1 ,azulejoUno)
                                            self.matrizUno.cambiar(i,j, azulejoUnoDerecha)
                                            print("azulejo " , i,",",j, "intercambio derechaUno")
                                            print("Se intercambiaron azulejos :D")
                                            self.crearGrafico()
                                        else:
                                            self.voltearPiso(i,j)

                                    
                                    else:
                                        self.voltearPiso(i,j)        
                                else:
                                    self.voltearPiso(i,j) 
                                     
                            elif   azulejoUnoDerecha != None:

                                    if azulejoUnoDerecha == azulejoDos: 
                                        if azulejoUnoDerecha != azulejoDosDerecha or (azulejoUnoDerecha == azulejoDosDerecha and int(self.F)*(2) > int(self.S)+int(self.F)) :

                                            self.precio += int(self.S)
                                            self.matrizUno.cambiar(i,j+1 ,azulejoUno)
                                            self.matrizUno.cambiar(i,j, azulejoUnoDerecha)
                                            print("azulejo " , i,",",j, "intercambio derechaDos")
                                            print("Se intercambiaron azulejos :D")
                                            self.crearGrafico()
                                        else:
                                            self.voltearPiso(i,j)
                                        
                                    else:
                                        self.voltearPiso(i,j)       
                            else:
                                self.voltearPiso(i,j)                                     
                        else:
                            self.matrizUno.switch(i,j) 
                            self.precio += int(self.F) 
                            print("Se voltearon los azulejos")
                            self.crearGrafico()

            
        return self.precio                    

    #para crear archivo de grafico 

    #creando grafico 
    def crearDot(self):
        grafico = 'digraph D {    node [shape=plaintext]      some_node [  label=<<table border="0" cellborder="1" cellspacing="0">'

        for i in range(int(self.R)):
                grafico += "<tr>"
                for j in range(int(self.C)):
                    contenido = self.matrizUno.buscar(i,j)
                    if contenido == "B":
                        grafico += '<td bgcolor="black">B</td>'
                    else:
                        grafico += '<td bgcolor="white">W</td>'
                grafico +=  "</tr> \n"
        grafico += '</table>> ]  ;  }'
        crearGrafico(grafico,"prueba1")
        path = 'C:/Users/pjbco/Desktop/1ER SEMESTRE 2022/IPC2/Practica1/IPC2_Proyecto1_201902698/prueba1.dot'
        s = Source.from_file(path)
        s.render('abcd.gv', format='jpg',view=False)

         
    def crearGrafico(self):
        for i in range(int(self.R)):
                separador = "|"

                for j in range(int(self.C)):
                    separador += self.matrizUno.buscar(i,j) + "|"
                print(separador)
                
                self.crearDot()
        input("presione Enter para continuar!!")
    
    def voltearPiso(self,i,j):
        self.matrizUno.switch(i,j) 
        self.precio += int(self.F) 
        print("Se voltearon los azulejos 2")
        self.crearGrafico()    

                    



                                    

                    

                    
        
    



                