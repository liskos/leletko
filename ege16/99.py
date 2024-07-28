import functools
@functools.lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if 0 < n < 3:
        return  1
    if n >= 3:
        return f(n - 2) + f(n - 1)

print(f(47))