import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException, StaleElementReferenceException

SELENIUM_URL = os.getenv("SELENIUM_URL", "http://selenium:4444/wd/hub")
SELENIUM_STATUS_URL = os.getenv("SELENIUM_STATUS_URL", "http://selenium:4444/wd/hub/status")
APP_URL = os.getenv("APP_URL", "http://csrf-lab:5000")

LOGIN_URL = f"{APP_URL}/login"
CHAT_URL = f"{APP_URL}/chat"

firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")

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

driver = webdriver.Remote(
    command_executor=SELENIUM_URL,
    options=firefox_options
)

def login_admin():
    print("[BOT] Iniciando sesión como admin...")
    try:
        driver.get(LOGIN_URL)
        time.sleep(2)

        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        username_field.send_keys("admin")
        password_field.send_keys("admin123")
        login_button.click()
        time.sleep(2)
        print("[BOT] Sesión iniciada correctamente.")
    except Exception as e:
        print(f"[BOT] Error durante el login: {e}")

def visitar_chat():
    try:
        driver.get(CHAT_URL)
        time.sleep(2)

        links = driver.find_elements(By.CSS_SELECTOR, ".mensaje-texto a")
        print(f"[BOT] Encontrados {len(links)} enlaces.")

        for index, link in enumerate(links):
            try:
                print(f"[BOT] Clicando enlace {index + 1}...")
                link.click()
                time.sleep(2)
                driver.get(CHAT_URL)
                time.sleep(2)
            except (WebDriverException, StaleElementReferenceException) as e:
                print(f"[BOT] Error haciendo click en enlace {index + 1}: {e}")
    except Exception as e:
        print(f"[BOT] Error al visitar el chat: {e}")

def ejecutar_tarea():
    login_admin()

    while True:
        print("[BOT] Visitando el chat...")
        visitar_chat()
        print("[BOT] Esperando 60 segundos antes de volver a visitar el chat...")
        time.sleep(60)

if __name__ == '__main__':
    try:
        ejecutar_tarea()
    except Exception as e:
        print(f"[BOT] Error crítico: {e}")
    finally:
        driver.quit()
