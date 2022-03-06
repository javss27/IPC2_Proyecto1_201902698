from xml.dom import minidom
from clases import ListaSimple
from tkinter.filedialog import askopenfilename
from clases import listaPatron

def leerArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    return contenido

def iniciarAnalisis():
    global ruta
    global doc
    ruta = askopenfilename()
    doc = minidom.parse(ruta)
    
    return inicial()    
         





def inicial():

    lista = ListaSimple()

    #Para obtener el nobre del piso
    piso = doc.getElementsByTagName("piso")[0]
    

    nombrePiso = doc.getElementsByTagName("piso")

    patronPiso = doc.getElementsByTagName("patrones")

    for pisosArtesanales in nombrePiso:
        patrones = listaPatron()
        sid = pisosArtesanales.getAttribute("nombre")

        filasPiso = pisosArtesanales.getElementsByTagName("R")[0]
        columnasPiso = pisosArtesanales.getElementsByTagName("C")[0]
        costoVolteo = pisosArtesanales.getElementsByTagName("F")[0]
        costoIntercambio = pisosArtesanales.getElementsByTagName("S")[0]


        
        nombre = sid 
        
        fila = filasPiso.firstChild.data
       
        columna = columnasPiso.firstChild.data
        
        volteo = costoVolteo.firstChild.data
        
        intercambio = costoIntercambio.firstChild.data

         
        
        for patron in pisosArtesanales.getElementsByTagName("patron"):
            valor = patron.firstChild.data.replace(" ","").replace("    ","").replace("\n","")
            codigo = patron.getAttribute("codigo")
            
            patrones.push( codigo, valor)


        lista.push( nombre,fila,columna,volteo,intercambio, patrones )
                     
    return lista

  

if __name__ == "__main__":
    inicial()


