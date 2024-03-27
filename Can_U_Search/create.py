
flag = "SOTI{StartFl@G_1s_Here!!!!!EndF1@g???!!!}"


import os
import random
import string

# 랜덤한 이름 생성
def generate_random_name():
    return ''.join(random.choices(string.ascii_letters, k=10))

# 랜덤한 길이의 문자열 생성
def generate_random_string():
    length = random.randint(200, 500)  # 200자에서 500자 사이의 길이
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

# 파일 생성
def create_file(directory):
    os.makedirs(directory, exist_ok=True)  # 디렉토리 생성

    for i in range(500):
        filename = os.path.join(directory, generate_random_name())
        with open(filename, 'w') as f:
            f.write(generate_random_string())

# 파일 생성 함수 호출
create_file('files')
