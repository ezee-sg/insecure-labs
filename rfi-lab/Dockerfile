FROM php:7.4-apache

RUN a2enmod rewrite

COPY php.ini /usr/local/etc/php/conf.d/custom.ini

COPY . /var/www/html/

RUN chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html

EXPOSE 80

CMD ["apache2-foreground"]
