def f(n):
    b = bin(n)[2:]
    c = b + b[-2] + b[1]
    return int(c, 2)


a = set()
for i in range(2, 100):
    if 150 <= f(i) >= 250:
        a.add(i)
print(f(11))
print(len(a))