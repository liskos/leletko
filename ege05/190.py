def f(a):
    b = bin(a)[2:]
    if b.count("1") > b.count("0"):
        b += "1"
    else:
        b += '0'
    return int(b, 2)


for i in range(1, 256):
    if f(i) > 36:
        print(f(i))
