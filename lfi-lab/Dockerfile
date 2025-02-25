# Usa una imagen oficial de PHP con Apache
FROM php:7.4-apache

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y libpng-dev libjpeg-dev libfreetype6-dev && \
    docker-php-ext-configure gd --with-freetype --with-jpeg && \
    docker-php-ext-install gd

# Habilitar el módulo de reescritura de Apache
RUN a2enmod rewrite

# Copiar los archivos de la aplicación al contenedor
COPY . /var/www/html/

# Dar permisos al directorio de imágenes (uploads)
RUN chmod -R 777 /var/www/html/uploads

# Exponer el puerto 80 para acceder a la aplicación
EXPOSE 80

# Configurar Apache para que apunte al directorio de tu aplicación
CMD ["apache2-foreground"]
