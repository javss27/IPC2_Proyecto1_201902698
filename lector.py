from xml.dom import minidom
doc = minidom.parse("datos.xml")

#Para obtener el nobre del piso
piso = doc.getElementsByTagName("piso")[0]
print(piso.firstChild.data)

nombrePiso = doc.getElementsByTagName("piso")
codigoPiso = doc.getElementsByTagName("patron")
patronPiso = doc.getElementsByTagName("patrones")

for pisosArtesanales in nombrePiso:
    sid = pisosArtesanales.getAttribute("nombre")

    filasPiso = pisosArtesanales.getElementsByTagName("R")[0]
    columnasPiso = pisosArtesanales.getElementsByTagName("C")[0]
    costoVolteo = pisosArtesanales.getElementsByTagName("F")[0]
    costoIntercambio = pisosArtesanales.getElementsByTagName("S")[0]


    print("nombre:%s " % sid)
    print("<R>:%s" % filasPiso.firstChild.data)
    print("<C>:%s" % columnasPiso.firstChild.data)
    print("<F>:%s" % costoVolteo.firstChild.data)
    print("<S>:%s" % costoIntercambio.firstChild.data)


for pisosArtesanales in codigoPiso:
    sid = pisosArtesanales.getAttribute("codigo")
    #sid = pisosArtesanales.getAttribute("patrones")

    
    print("codigo:%s " % sid)   
    #print("patrones:%s" % sid)
    
for pisosArtesanales in patronPiso:
    sid = pisosArtesanales.getAttribute("patrones")

    patron =pisosArtesanales.getElementsByTagName("patrones")
    for patrones in patron:
        codigoDosPiso = patrones.getElementsByTagName("patron")[0]
        print("patrones:%s" % codigoDosPiso.firstChild.data)
