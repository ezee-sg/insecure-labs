## 🚨 noSQL Injection (noSQLi-Lab)
- Aplicación que simula un login de acceso a un panel de administrador.
- Presenta una vulnerabilidad a inyección noSQL en el formulario de login.

Si un usuario malintencionado cambia la cabecera **Content-Type** de **application/x-www-form-urlencoded** a **application/json** y pega el siguiente payload como cuerpo de la peticion, puede hacer bypass del login, accediendo de esta forma al panel de administrador sin disponer de credenciales válidas.

El payload sería este:
```sh
{

	"username":{"$ne":"invalid"},

	"password": {"$ne":"invalid"}

}
```