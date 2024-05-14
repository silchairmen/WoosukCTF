FROM python:3.9-slim-buster

WORKDIR /app

COPY app.py .
COPY templates/index.html templates/
COPY static/style.css static/
COPY FLAG .

RUN pip install Flask

EXPOSE 80

CMD ["python", "app.py"]