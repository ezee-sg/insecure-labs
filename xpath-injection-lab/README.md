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