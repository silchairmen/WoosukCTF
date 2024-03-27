FROM php:7.3.3-apache

COPY ./flag.txt /flag.txt
COPY /deploy/public/ /var/www/html/

RUN chmod 777 /flag.txt

EXPOSE 80