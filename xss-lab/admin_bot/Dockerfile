# Imagen base de Python
FROM python:3.9

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && apt-get clean

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando por defecto
CMD ["python", "admin_bot.py"]
