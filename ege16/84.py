import functools
@functools.lru_cache(None)
def f(n, m):
    if m == 0:
        return 10 ** 7
    if n < 2:
        return n
    if n >= 2 and n % 2 == 0:
        return f(n // 2, m - 1) + 1
    if n >= 2 and n % 2 != 0:
        return f(3 * n + 1, m - 1) + 1

a = set()
for i in range(1, 101):
    if 100 < f(i, 1000) < 10 ** 7:
        a.add(i)

print(len(a))
