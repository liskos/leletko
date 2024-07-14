import functools
@functools.lru_cache(None)
def f(n, m):
    if m == 0:
        return 10 ** 7
    if n <= 5:
        return n
    if n > 5 and n % 8 == 0:
        return n + f(n // 2 - 3, m - 1)
    if n > 5 and n % 8 != 0:
        return n +f(n + 4, m - 1)


for i in range(1, 100000):
    if f(i, 100) < 10 ** 7:
        print(i, f(i, 100))