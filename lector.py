from xml.dom import minidom
from clases import ListaSimple
from tkinter.filedialog import askopenfilename

def leerArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    return contenido

def iniciarAnalisis():
    global ruta
    ruta = askopenfilename()
         

doc = minidom.parse("datos.xml")




def inicial():

    lista = ListaSimple()
    #Para obtener el nobre del piso
    piso = doc.getElementsByTagName("piso")[0]
    print(piso.firstChild.data)

    nombrePiso = doc.getElementsByTagName("piso")

    patronPiso = doc.getElementsByTagName("patrones")

    for pisosArtesanales in nombrePiso:
        sid = pisosArtesanales.getAttribute("nombre")

        filasPiso = pisosArtesanales.getElementsByTagName("R")[0]
        columnasPiso = pisosArtesanales.getElementsByTagName("C")[0]
        costoVolteo = pisosArtesanales.getElementsByTagName("F")[0]
        costoIntercambio = pisosArtesanales.getElementsByTagName("S")[0]


        print("nombre:%s " % sid)
        nombre = sid 
        print("<R>:%s" % filasPiso.firstChild.data)
        fila = filasPiso.firstChild.data
        print("<C>:%s" % columnasPiso.firstChild.data)
        columna = columnasPiso.firstChild.data
        print("<F>:%s" % costoVolteo.firstChild.data)
        volteo = costoVolteo.firstChild.data
        print("<S>:%s" % costoIntercambio.firstChild.data)
        intercambio = costoIntercambio.firstChild.data

        codigoDosPiso = pisosArtesanales.getElementsByTagName("patron")[0]
        print("patrones:%s" % codigoDosPiso.firstChild.data)
        patronUno = codigoDosPiso.firstChild.data

        codigoPiso1 = codigoDosPiso.getAttribute("codigo")
        print("codigo:%s " % codigoPiso1)
        piso1 = codigoPiso1

        codigoDosPiso = pisosArtesanales.getElementsByTagName("patron")[1]
        print("patrones:%s" % codigoDosPiso.firstChild.data)
        patronDos = codigoDosPiso.firstChild.data

        codigoPiso1 = codigoDosPiso.getAttribute("codigo")
        print("codigo:%s " % codigoPiso1)
        piso2 = codigoPiso1

        lista.push( nombre, piso1, piso2 ,fila,columna,volteo,intercambio, patronUno, patronDos)
                     
    lista.imprimir()

  

if __name__ == "__main__":
    inicial()


