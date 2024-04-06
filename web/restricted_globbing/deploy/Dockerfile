FROM python:3.10-slim-buster

ENV USER soti
ENV PORT 80

RUN apt-get update -y && apt-get install -y python3-pip build-essential curl
RUN apt-get install -y sqlite3

RUN pip install --upgrade pip
RUN adduser --disabled-password $USER

WORKDIR /app

COPY ./deploy /app
COPY ./flag.txt /flag.txt
RUN chmod +r /flag.txt
RUN pip install flask


#db
COPY ./init.sql /init.sql

RUN sqlite3 user.db < /init.sql

EXPOSE $PORT

ENTRYPOINT [ "python" ]
CMD ["app.py"]
