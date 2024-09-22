def pr(n):
    b = n
    a = ""
    c = "0123456789ab"
    while b > 0:
        a = a + c[b % 12]
        b = b // 12
    return a[::-1]


def f(n):
    a = pr(n)
    if n % 3 == 0:
        a = "1" + a + "b"
    else:
        a = "2" + a + "0"
    return int(a, 12)

print(f(11))
print(f(12))
a = set()
for i in range(1, 10000):
    if f(i) < 1996:
        a.add(f(i))
print(max(a))