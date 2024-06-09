FROM php:7.4-apache

USER root
COPY ./deploy /var/www/html/

RUN mkdir /var/www/html/uploads
RUN chmod 777 /var/www/html/uploads

COPY ./flag /flag
RUN chmod 444 /flag

RUN echo "AddType application/x-httpd-php .php .phar" >> /etc/apache2/apache2.conf

RUN docker-php-ext-install mysqli
RUN a2enmod rewrite
