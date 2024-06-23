def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        c = b[-4] + b[-3] + b[-2] + b[-1]
        c = c.replace("1", "2")
        c = c.replace("0", "1")
        c = c.replace("2", "0")
        b = b[:-4] + c
    else:
        c = b[1:5]
        c = c.replace("1", "2")
        c = c.replace("0", "1")
        c = c.replace("2", "0")
        b = b[0] + c + b[5:]
    return int(b, 2)


print(f(36))
print(f(37))
a = set()
for i in range(64, 1000):
        print(i, f(i))
        a.add(f(i))
print(min(a))


