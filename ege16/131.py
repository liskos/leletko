import sys
sys.setrecursionlimit(10000)
import functools
@functools.lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)

a = f(2023)
b = f(2020)
print(a / b)
