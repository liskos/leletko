a = 203
b = bin(a)[2:]
b = b.zfill(8)
b = b.replace("1", "2")
b = b.replace("0", "1")
b = b.replace("2", "0")
print(int(b, 2))