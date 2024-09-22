def pr(n):
    b = ""
    c = "0123456789ab"
    while n > 0:
        b += c[n % 12]
        n //= 12
    return b[::-1]


def f(n):
    b = pr(n)
    if n % 4 == 0:
        b = "2" + b + "64"
    else:
        b = b + max(b)
    return int(b, 12)

print(f(11))
a = set()
for i in range(1, 1000):
    if f(i) > 1799:
        a.add(f(i))
print(min(a))
