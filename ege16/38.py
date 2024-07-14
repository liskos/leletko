def f(n, m):
    if m == 0:
        d = 0
    else:
        d = n + f(n, m - 1)
    return d


a = set()
for i in range(1, 100):
    for c in range(1, 100):
            if f(i, c) == 30:
                a.add(i)
print(len(a))