import sys
sys.setrecursionlimit(10000)
import functools
@functools.lru_cache(None)
def f(n):
    if n < 4 or n % 2 != 0:
        return 1
    if n > 3 and n % 2 == 0:
        return f(n - 1) + f(n - 2) + f(n -3)

print(f(2008) - f(2006))