import functools
@functools.lru_cache(None)
def f(n, m):
    if m == 0:
        return  10 ** 7
    if n <= 5:
        return n
    if n > 5 and n % 4 == 0:
        return n + f(n // 2 - 1, m - 1)
    if n > 5 and n % 4 != 0:
        return n + f(n + 2, m - 1)

for i in range(1, 10000000):
    if f(i, 100) < 10 ** 7:
        print(i, f(i, 100))