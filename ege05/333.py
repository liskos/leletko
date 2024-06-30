def pr(n):
    b = ""
    while n > 0:
        b = b + str(n % 3)
        n = n // 3
    return b[::-1]


def f(n):
    b = pr(n)
    if n % 3 == 0:
        b = b + b[-2] + b[-1]
    else:
        b = b + str(pr(n % 3 * 5))
    return int(b, 3)


print(f(11))
print(f(12))
a = set()
for i in range(1, 1000):
    if f(i) > 133:
        a.add(f(i))
print(min(a))

