def f(n):
    b = bin(n)[2:]
    a = b.count("1")
    c = b.count("0")
    if a > c:
        b += "1"
    else:
        b += "0"
    return int(b, 2)

for i in range(1, 50):
    if f(i) < 43:
        print(f(i))