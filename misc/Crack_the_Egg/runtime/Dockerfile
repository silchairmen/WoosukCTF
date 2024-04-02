FROM python:3-alpine

ENV user chall
ENV port 5000

RUN apk add --no-cache bash 

RUN adduser --disabled-password $user
ADD ./deploy /app
WORKDIR /app
RUN pip install -r requirements.txt

USER $user
EXPOSE $port

ENTRYPOINT ["python"]
CMD ["app.py"]