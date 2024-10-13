def f(n):
    b = ""
    while n > 0:
        b = b + str(n % 4)
        n = n // 4
    return b[::-1]

def g(n):
    b = f(n)
    if n % 4 == 0:
        b = b + b[:2]
    else:
        b = b + f(4 * (n % 4))
    return int(b, 4)

print(g(11))
print(g(12))
a = set()
for i in range(1, 100):
    if g(i) > 291:
        a.add(g(i))
print(min(a))