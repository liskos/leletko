def f(n):
    b = bin(n)[2:]
    d = b[:-2]
    return int(d, 2)

a = set()
for i in range(20, 601):
    a.add(f(i))
print(len(a))
