def fa(n):
    if n == 1:
        return 1
    else:
        return n * f(n - 1)
import sys
sys.setrecursionlimit(10000)
import functools
@functools.lru_cache(None)
def f(n):
    if n >= 5000:
        return fa(n)
    if 1 <= n <= 5000:
        return 2 * f(n + 1) / (n + 1)

print(1000 * f(7) / f(4))