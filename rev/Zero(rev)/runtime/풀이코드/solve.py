def check(c):
    return c == 0x70

def genKey(c):
    if check(c):
        return c ^ 0x46
    else:
        return (((c - 32) + 73) % 95 +32)
		
def encrypt(a, b):
    return (a - b) % 256
    
KEY = 'ue~uo&,u}Fju+~HuaH0u'

v3 = []

for i in range(20):
    v3.append(genKey(ord(KEY[i])))

with open('flag.txt', 'r') as f:
    line = f.readline()

    hex_list = [int(line[i:i+2], 16) for i in range(0, len(line), 2)]
    
    for i in range(9):
        for j in range(len(hex_list)):
            hex_list[j] = encrypt(hex_list[j], v3[i % 9])
        
    for i in hex_list:
            print(chr(i), end='')