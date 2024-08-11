def p(n):
    a = ""
    while n > 0:
        a = a + str(n % 8)
        n = n // 8
    return a[::-1]


def f(n):
    b = p(n)
    a = sorted(b)
    if n % 2 == 0:
        b = b + p(int(a[-1]))
    else:
        b = b + p((int(a[0]) * 2))
    return int(b, 8)

print(f(9))
print(f(12))
for i in range(1, 1000):
    if f(i) < 313:
        print(i)
