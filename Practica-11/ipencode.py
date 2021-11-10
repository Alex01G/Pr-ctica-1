import socket
import logging
from base64 import b64encode

fo = open("encode.txt", "w")

def ip():
    logging.basicConfig(filename="ipencode.log", level=logging.INFO)
    nombre = socket.gethostname()
    ipequip = socket.gethostbyname(nombre)
    s = str(ipequip)
    enip = b64encode(s.encode("utf-8"))
    print("La ip codificada es:", enip)
    fo.write("Ip codificada:\n")
    fo.write(str(enip))
    logging.info("Se ha ejecutado correctamente")

domain = "www.google.com"
def pubdomain():
    ipdomain = socket.gethostbyname(domain)
    st = str(ipdomain)
    doenip = b64encode(st.encode("utf-8"))
    print("La Ip de dominio codificada es:", doenip)
    fo.write("\n\nIp de dominio codificada:\n")
    fo.write(str(doenip))
	

ip()
pubdomain()
    
fo.close()