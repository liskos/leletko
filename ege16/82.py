import functools
@functools.lru_cache(None)
def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 4 == 0:
        return n + f(n / 2 - 1)
    if n > 5 and n % 4 != 0:
        return 1

for i in range(1, 10000000):
        print(f(i))