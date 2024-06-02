def f(n):
    b = bin(n)[2:]
    b = int(b.replace('0', ''))
    b = str(b)
    return int(b, 2)

a = set()
for i in range(10, 2500):
    a.add(f(i))
print(len(a))
