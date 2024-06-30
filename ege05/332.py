def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        c = b + "0"
    else:
        c = b + "1"
    if b.count("1") % 2 == 0:
        c = c + "0"
    else:
        c = c + "1"
    return int(c, 2)

print(f(13))
print(f(10))
a = set()
for i in range(1, 1000):
    if f(i) > 2023:
        a.add(f(i))
print(min(a))

