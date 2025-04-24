import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options

SELENIUM_URL = os.getenv("SELENIUM_URL", "http://selenium:4444/wd/hub")
SELENIUM_STATUS_URL = os.getenv("SELENIUM_STATUS_URL", "http://selenium:4444/wd/hub/status")
APP_URL = os.getenv("APP_URL", "http://xss-lab:5000")

LOGIN_URL = f"{APP_URL}/login"
ADMIN_PAGE = f"{APP_URL}/admin/messages"

# Configuración de navegador
firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")

# Esperar hasta que Selenium esté realmente listo
print("[BOT] Esperando a que Selenium esté disponible...")
while True:
    try:
        resp = requests.get(SELENIUM_STATUS_URL)
        if resp.status_code == 200 and resp.json().get("value", {}).get("ready", False):
            print("[BOT] Selenium está listo.")
            break
    except Exception:
        pass
    time.sleep(2)

# Conectar con WebDriver
driver = webdriver.Remote(
    command_executor=SELENIUM_URL,
    options=firefox_options
)

def ejecutar_tarea():
    print("[BOT] Iniciando sesión como admin...")
    driver.get(LOGIN_URL)
    time.sleep(2)

    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_field.send_keys("admin")
    password_field.send_keys("admin123")
    login_button.click()

    time.sleep(2)

    while True:
        print("[BOT] Visitando la página de mensajes...")
        driver.get(ADMIN_PAGE)
        print("[BOT] Tarea completada.")
        print("[BOT] Esperando 60 segundos para la siguiente ejecución...")
        time.sleep(60)

if __name__ == '__main__':
    #ejecutar_tarea()
