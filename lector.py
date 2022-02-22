import xml.etree.ElementTree as ET

try:
    xml_file = open('datos.xml')
    if xml_file.readable():
        xml_data = ET.fromstring(xml_file.read())
        print(xml_data)
    else:
        print(False)
except Exception as err:
        print("Error:", err)
finally:
        xml_file.close()