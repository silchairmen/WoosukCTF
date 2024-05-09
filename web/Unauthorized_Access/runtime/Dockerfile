# 베이스 이미지 설정
FROM python:3.8-slim-buster

# 작업 디렉토리 설정
WORKDIR /app

RUN apt-get update -y && apt-get install -y python3-pip build-essential

# 현재 디렉토리의 모든 파일을 컨테이너의 /app 디렉토리로 복사
COPY . /app

# Flask 및 Flask-CORS 및 다른 의존성 설치
RUN pip install flask flask-cors

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD ["app.py"]