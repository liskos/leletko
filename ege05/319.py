def f(n):
    b = bin(n)[2:]
    if n % 10 == 0:
        b = b +  b[-4] + b[-3] + b[-2] + b[-1]
    else:
        b = b + str(bin( int(b[-1]) // 2)[2:])
    return int(b, 2)

print(f(11))
print(f(20))
a = set()
for i in range(5, 1000):
    if f(i) < 680:
        a.add(i)
print(len(a))