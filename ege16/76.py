import functools
@functools.lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return 3 + f(n // 2 - 1)
    if n > 1 and n % 2 != 0:
        return 100000

for i in range(1, 100000):
    if f(i) == 19:
        print(i)
        break