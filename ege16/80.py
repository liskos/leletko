import functools
@functools.lru_cache(None)
def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 3 == 0:
        return n + f(n // 3 + 2)
    if n > 5 and n % 3 != 0:
        return 10 ** 7

for i in range(1, 100000):
    if 1000 < f(i) < 10 ** 7:
        print(i)
        break