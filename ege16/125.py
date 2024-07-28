def s(n):
    a = 0
    while n > 0:
        a = a + n % 10
        n = n // 10
    return a


import functools
@functools.lru_cache(None)
def f(n):
    if n < 3:
        return 1
    if n > 2 and s(n) % 2 == 0:
        return f(n - 1) - f(n - 2)
    if n > 2 and s(n) % 2 != 0:
        return  f(n - 1) + f(n // 2)


print(f(100))