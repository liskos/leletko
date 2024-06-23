def f(n):
    n = str(n)
    if int(n[0]) % 2 == 0:
        b = int(n[0]) + int(n[2]) + abs(int(n[1]) - int(n[3]))
    else:
        b = sorted(n)
        b = "".join(b)
        b = int(b[0] + b[1] + b[2] + b[3])
        b = bin(b)[2:]
        b = b.count("1")
    return b

a = set()
for i in range(1000, 10000):
    if f(i) > 20:
        a.add(i)

print(len(a))