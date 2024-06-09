FROM php:7.4-apache
COPY ./deploy /var/www/html/

RUN chmod 777 /var/www/html/uploads

COPY ./flag /flag
RUN chmod 444 /flag

RUN docker-php-ext-install mysqli
RUN a2enmod rewrite
