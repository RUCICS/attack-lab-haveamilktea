# test3.py
#!/usr/bin/env python3

# 先创建一个64字节的文件
payload = b"A" * 64

with open("ans3.txt", "wb") as f:
    f.write(payload)

print("Created ans3.txt with 64 'A's")