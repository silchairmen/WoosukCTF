import struct

KEY = "Encryted Jalnik's File KKKKKKK"
KEY_LEN = len(KEY)

with open('flag_en.png', 'rb') as file:
    with open('flag_de.png', 'wb') as sol:
        content = file.read()
        
        for i in range(len(content)):
            s = content[i] ^ ord(KEY[i % KEY_LEN])
            print(".")
            sol.write(struct.pack('B', s))
