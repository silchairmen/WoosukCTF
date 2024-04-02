FROM php:7.3.3-apache
COPY /web/public/ /var/www/html/
COPY ./flag.txt /flag.txt

RUN chmod 777 /flag.txt
RUN cat ./flag.txt >> /var/www/html/index.php
RUN rm -rf /flag.txt

EXPOSE 80