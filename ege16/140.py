import sys
sys.setrecursionlimit(10000)
import functools
@functools.lru_cache(None)
def f(n):
    if n > 10000:
        return n - 10000
    if 1 <= n <= 10000:
        return f(n + 1 ) + f(n + 2)

print(f(12345) * (f(10) - f(12)) / f(11) + f(10101))