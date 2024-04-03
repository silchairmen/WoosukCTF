FROM python:3-alpine

ADD ./flag.txt /flag.txt

RUN cat /flag.txt >> /etc/passwd

ENV user soti
ENV port 80

RUN apk add --no-cache bash 

RUN adduser --disabled-password $user
RUN mkdir /app

ADD ./deploy /app

WORKDIR /app
RUN pip install -r requirements.txt

# important!
RUN chmod 444 /flag.txt

USER $user
EXPOSE $port

ENTRYPOINT ["python"]
CMD ["app.py"]