def f(n):
    b = bin(n)[2:]
    if n % 10 == 0:
        b = b + b[-4:]
    else:
        b = b + bin( int(str(n)[-1]) ** 2 // 2)[2:]
    return int(b, 2)

print(f(11))
print(f(20))
a = set()
for i in range(11, 1000):
    if f(i) < 680:
        a.add(i)
print(len(a))