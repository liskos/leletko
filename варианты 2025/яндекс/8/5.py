def per(n):
    b = ""
    while n > 0:
        b = b + str(n%3)
        n = n // 3
    return b[::-1]

def f(n):
    b = per(n)
    if b.count("2") == 0:
        b = b + "0"
    else:
        b = b + per(b.count("2"))
    if b.count("1") == 0:
        b = b + "0"
    else:
        b = b + per(b.count("1"))
    if b.count("0") == 0:
        b = b + "0"
    else:
        b = b + per(b.count("0"))
    return int(b,3)

for i in range(1,10000):
    if f(i) < 1000:
        print(i)
