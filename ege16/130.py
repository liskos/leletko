import functools
@functools.lru_cache(None)
def f(n):
    if n < 3:
        return 3 * n
    if n > 2 and n % 2 == 0:
        return f( n- 2) * f(n - 1) - n
    if n > 2 and n % 2 != 0:
        return  f( n - 1) - f(n - 2) + 2 * n


a = str(f(30))
print(a[-2:])