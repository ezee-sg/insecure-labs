import os, signal, sys, time, re
from termcolor import colored

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# CTRL + C
def def_handler(sig, frame):
    print(colored("\n\n👋  Saliendo del programa...\n\n", "yellow"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# Diccionario con los nombres de los laboratorios y sus rutas
laboratorios = {
    "1": ("Deserialization Lab", "deserialization-lab"),
    "2": ("LFI Lab", "lfi-lab"),
    "3": ("Log Poisoning Lab", "log-poisoning-lab"),
    "4": ("NoSQLi Lab", "nosqli-lab"),
    "5": ("RFI Lab", "rfi-lab"),
    "6": ("SQLi Lab", "sqli-lab"),
    "7": ("SSRF Lab", "ssrf-lab"),
    "8": ("SSTI Lab", "ssti-lab"),
    "9": ("XXE Lab", "xxe-lab"),
    "10": ("LaTeX Injection Lab", "latex-injection-lab"),
    "11": ("XPath Injection Lab", "xpath-injection-lab"),
}

# Obtiene el puerto de un laboratorio
def obtener_puerto(ruta):
    compose_file = f"{ruta}/docker-compose.yml"
    if not os.path.exists(compose_file):
        return "N/A"
    
    with open(compose_file, 'r') as file:
        contenido = file.read()
    
    match = re.search(r'\s*-\s*"(\d+):\d+"', contenido)
    return match.group(1) if match else "N/A"

def obtener_contenedores_activos():
    activos = {}
    for key, (_, ruta) in laboratorios.items():
        estado = os.popen(f"docker compose -f {ruta}/docker-compose.yml ps --services").read().strip()
        if estado:
            activos[key] = obtener_puerto(ruta)
    return activos

def mostrar_menu():
    clear_screen()
    activos = obtener_contenedores_activos()
    print(colored("\n\n--- Selecciona una opción ---\n", "cyan"))
    for key, (nombre, _) in laboratorios.items():
        if key in activos:
            estado = colored("✔", "green")
            puerto = colored(f"(http://127.0.0.1:{activos[key]})",'green')
        else:
            estado = colored("✘", "red")
            puerto = ""
        print(f"{key}. {nombre} {estado} {puerto}")
    print(colored("x. Detener todos los laboratorios activos", "red"))
    print(colored("0. Salir", "yellow"))

def barra_progreso():
    for i in range(1, 101, 2):
        sys.stdout.write(f"\r[{colored('=' * (i // 2), 'green')}{' ' * (50 - i // 2)}] {i}%")
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write(f"\r[{colored('=' * 50, 'green')}] 100%\n")
    sys.stdout.flush()

def desplegar_laboratorio(opcion):
    if opcion in laboratorios:
        nombre, ruta = laboratorios[opcion]
        print(colored(f"\n\n🔹 Desplegando {nombre}...\n", "blue"))
        os.system(f"docker compose -f {ruta}/docker-compose.yml up --build -d")
        barra_progreso()
    else:
        print(colored("\n\n⚠️  Opción no válida.\n\n", "red"))
        time.sleep(2)

def detener_todos():
    activos = obtener_contenedores_activos()
    if not activos:
        print(colored("\n\n⚠️  No hay laboratorios activos para detener.\n\n", "yellow"))
        return
    
    print(colored("\n\n🛑  Deteniendo laboratorios activos...\n\n", "red"))
    for key in activos.keys():
        _, ruta = laboratorios[key]
        os.system(f"docker compose -f {ruta}/docker-compose.yml down --rmi all --volumes --remove-orphans")
    
    barra_progreso()

def main():
    while True:
        mostrar_menu()
        opcion = input(colored("\nSelecciona una opción: ", "cyan")).strip().lower()
        
        if opcion == "0":
            print(colored("\n\n👋  Saliendo del programa...\n\n", "yellow"))
            break
        elif opcion == "x":
            detener_todos()
        else:
            desplegar_laboratorio(opcion)

if __name__ == "__main__":
    main()
