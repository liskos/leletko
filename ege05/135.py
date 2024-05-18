def f(n):
    b = bin(n)[2:]
    s1, s2, s3, s4, = str(n)
    a1 = int(s1) + int(s2)
    a2 = int(s2) + int(s3)
    a3 = int(s3) + int(s4)
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    return int(b, 2)

for i in range(1, 1000):
    if f(i)<125:
        print(f(i))