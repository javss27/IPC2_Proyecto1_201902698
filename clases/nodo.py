from .matriz import matriz
from .grafico import guardarDot
from graphviz import render
from graphviz import Source
import os
from os import remove

class Nodo:
    def __init__(self, siguiente,  nombrePiso, R,C,F,S, listaPatrones):
        self.setSiguiente(siguiente)
        self.setValor(  nombrePiso, R,C,F,S, listaPatrones)

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def setValor(self, nombrePiso, R,C,F,S, listaPatrones):
        self.listaPatrones = listaPatrones
        self.nombrePiso = nombrePiso
        self.R = R
        self.C = C
        self.F = F #costo por volteo
        self.S = S #Costo por cambio
        self.grafico =""
        self.numero = 0
        
        self.matrizUno = matriz()
        self.matrizDos = matriz()
        self.precio = 0

    def limpiar(self):
       
        self.numero =0 
        self.precio = 0
        self.matrizUno = matriz()
        self.matrizDos = matriz()
        self.grafico = "digraph D {    node [shape=plaintext]"
        
        
    def calcular(self,consola):
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
                                        self.crearGrafico(consola)
                                    else:
                                        self.voltearPiso(i,j,consola)

                                elif  azulejoUnoDerecha != None:
                                    if azulejoUnoDerecha == azulejoDos:
                                        if azulejoUnoDerecha != azulejoDosDerecha or (azulejoUnoDerecha == azulejoDosDerecha and int(self.F)*(2) > int(self.S)+int(self.F)):
                                            self.precio += int(self.S)
                                            self.matrizUno.cambiar(i,j+1 ,azulejoUno)
                                            self.matrizUno.cambiar(i,j, azulejoUnoDerecha)
                                            print("azulejo " , i,",",j, "intercambio derechaUno")
                                            print("Se intercambiaron azulejos :D")
                                            self.crearGrafico(consola)
                                        else:
                                            self.voltearPiso(i,j,consola)

                                    
                                    else:
                                        self.voltearPiso(i,j,consola)        
                                else:
                                    self.voltearPiso(i,j,consola) 
                                     
                            elif   azulejoUnoDerecha != None:

                                    if azulejoUnoDerecha == azulejoDos: 
                                        if azulejoUnoDerecha != azulejoDosDerecha or (azulejoUnoDerecha == azulejoDosDerecha and int(self.F)*(2) > int(self.S)+int(self.F)) :

                                            self.precio += int(self.S)
                                            self.matrizUno.cambiar(i,j+1 ,azulejoUno)
                                            self.matrizUno.cambiar(i,j, azulejoUnoDerecha)
                                            print("azulejo " , i,",",j, "intercambio derechaDos")
                                            print("Se intercambiaron azulejos :D")
                                            self.crearGrafico(consola)
                                        else:
                                            self.voltearPiso(i,j,consola)
                                        
                                    else:
                                        self.voltearPiso(i,j,consola)       
                            else:
                                self.voltearPiso(i,j,consola)                                     
                        else:
                            self.matrizUno.switch(i,j) 
                            self.precio += int(self.F) 
                            print("Se voltearon los azulejos")
                            self.crearGrafico(consola)

        self.crearPatronFinal()
        return self.precio                    

    #para crear archivo de grafico 

    #creando grafico 
    def crearDot(self):
        
     
        self.numero += 1
        
        self.grafico += 'some_node' + str(self.numero) + ' [  label=<<table border="0" cellborder="1" cellspacing="0">'

        for i in range(int(self.R)):
                self.grafico += "<tr>"
                for j in range(int(self.C)):
                    contenido = self.matrizUno.buscar(i,j)
                    if contenido == "B":
                        self.grafico += '<td bgcolor="black">B</td>'
                    else:
                        self.grafico += '<td bgcolor="white">W</td>'
                self.grafico +=  "</tr> \n"
        self.grafico += '</table>> ]  ; '

       

         
    def crearGrafico(self, pasosEnConsola,):
        if pasosEnConsola:
            for i in range(int(self.R)):
                separador = "|"


                for j in range(int(self.C)):
                    separador += self.matrizUno.buscar(i,j) + "|"
                print(separador)
            input("presione Enter para continuar!!")

        else:
            self.crearDot()
        
    

        
    def voltearPiso(self,i,j, consola):
        self.matrizUno.switch(i,j) 
        self.precio += int(self.F) 
        print("Se voltearon los azulejos 2")
        self.crearGrafico(consola)    

    def imprimirMatrizUno(self):
        for i in range(int(self.R)):
                separador = "|"

                for j in range(int(self.C)):
                    separador += self.matrizUno.buscar(i,j) + "|"
                print(separador)

    def imprimirMatrizDos(self):
        for i in range(int(self.R)):
                separador = "|"

                for j in range(int(self.C)):
                    separador += self.matrizDos.buscar(i,j) + "|"
                print(separador)

    def crearPasos(self):
        self.grafico += "}"
        guardarDot(self.grafico,"prueba1")
        path = 'C:/Users/pjbco/Desktop/1ER SEMESTRE 2022/IPC2/Practica1/IPC2_Proyecto1_201902698/prueba1.dot'
        s = Source.from_file(path)
        s.render('prueba1', format='jpg',view=True)
        remove("prueba1")

    def crearPatronFinal(self):
        
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

        guardarDot(grafico,"patronFinal")
        path = 'C:/Users/pjbco/Desktop/1ER SEMESTRE 2022/IPC2/Practica1/IPC2_Proyecto1_201902698/patronFinal.dot'
        s = Source.from_file(path)
        s.render('patronFinal', format='jpg',view=True)
        remove("patronFinal")




                                    

                    

                    
        
    



                