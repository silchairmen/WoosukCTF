# 베이스 이미지 설정
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 현재 디렉토리의 모든 파일을 컨테이너의 /app 디렉토리로 복사
COPY . /app

# Flask 및 Flask-CORS 및 다른 의존성 설치
RUN pip install Flask Flask-CORS

# 포트 5000을 노출
EXPOSE 5000

# 컨테이너 실행 시 실행될 명령
CMD ["python", "app.py"]