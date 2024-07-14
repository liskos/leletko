def f(n, m):
    if n < m:
        n, m = m, n
    if n != m:
        return f(n - m, m)
    else:
        return n

for n in range(1, 100):
    for m in range(1, 100):
        if f(n, m) > 15 and n + m < 50 and n != m:
            print(n, m, f(n, m), )
