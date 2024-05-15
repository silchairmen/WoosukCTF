encrypt = "CuhbXbV3WLbPhpehuBKdKDKC"

def decode_string(input_str):
    decode_str = ""
    for char in input_str:
        decode_str += chr(ord(char) - 3)
    
    return decode_str


if __name__=="__main__":
    flag = decode_string(encrypt)

    print(flag)