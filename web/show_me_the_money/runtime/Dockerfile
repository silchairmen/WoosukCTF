# 베이스 이미지 선택 (Python 3.9)
FROM python:3.9-slim-buster

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY app.py .
COPY templates/index.html templates/
COPY static/style.css static/
COPY FLAG .

# 필요한 패키지 설치
RUN pip install Flask

# 포트 설정
EXPOSE 80

# 애플리케이션 실행
CMD ["python", "app.py"]