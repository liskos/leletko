def s(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
import functools
@functools.lru_cache(None)

def f(n):
    if n == 0:
        return 1
    if n > 0:
        return 2 * f(1 - n) + 3 * f(n - 1) + 2
    if n < 0:
        return -f(-n)

print(s(f(50)))