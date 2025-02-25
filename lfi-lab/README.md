## 🚨 Local File Inclusion (LFI-Lab)
- Aplicación vulnerable a inclusión de archivos locales del servidor mediante la descarga de imágenes.
- Esta vulnerabilidad puede ser crítica ya que podemos leer archivos con información confidencial que no deberíamos poder ver. 

El parámetro **image** empleado a la hora de descargar archivos es manipulable de forma que podemos ir hacia atrás varios directorios (Directory Path Traversal).

En este ejemplo estamos leyendo el archivo **/etc/passwd** del servidor: 

```sh
GET /download_image.php?image=../../../../../../../etc/passwd
```
