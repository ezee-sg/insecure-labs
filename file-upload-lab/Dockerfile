FROM php:7.4-apache

RUN apt-get update && apt-get install -y libpng-dev libjpeg-dev libfreetype6-dev && \
    docker-php-ext-configure gd --with-freetype --with-jpeg && \
    docker-php-ext-install gd

RUN docker-php-ext-install mysqli pdo pdo_mysql


RUN a2enmod rewrite

COPY . /var/www/html/

RUN chmod -R 777 /var/www/html/uploads

EXPOSE 80

CMD ["apache2-foreground"]