def f(n, m):
    if m == 0:
        return n
    else:
        return f(m, n % m)

a = set()
for n in range(100, 1001):
    for m in range(100, 1001):
        if f(n, m) == 30:
            a.add(n)
print(len(a))