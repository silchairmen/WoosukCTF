flag = "@re_U_S0TI_Member?"

def encode_string(input_str):
    encoded_str = ""
    for char in input_str:
        encoded_str += chr(ord(char) + 3)  # ASCII 코드 값에 3을 더하여 새로운 문자열 생성
    return encoded_str

# 주어진 문자열
flag = "@re_U_S0TI_Member?HaHAH@"

# 인코딩된 문자열 출력
encoded_flag = encode_string(flag)
print(encoded_flag)
