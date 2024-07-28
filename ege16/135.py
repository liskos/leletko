import sys
sys.setrecursionlimit(10000)
import functools
@functools.lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)

print(int(f(1000) / f(997)))