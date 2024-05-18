def f(n):
    b = bin(n)[2:]
    if sum(map(int, b )) % 2 == 0:
        b += "1"
    else:
        b += "0"
    if sum(map(int, b )) % 2 == 0:
        b += "1"
    else:
        b += "0"
    return int(b, 2)

a = set()
for i in range(1, 1000):
    if 16 <= f(i) <= 32:
        a.add(f(i))
print(a)
print(len(a))