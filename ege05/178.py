a = 95
b = bin(a)[2:]
b = b.replace("1", "2")
b = b.replace("0", "1")
b = b.replace("2", "0")
b = b + "1"
print(int(b, 2))