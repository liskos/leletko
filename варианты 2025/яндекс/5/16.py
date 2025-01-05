import sys
sys.setrecursionlimit(10000)
import functools
@functools.lru_cache(None)

def f(n):
    if n >= 2025:
        return 1
    if n < 2025:
        return n - f(n+2) - f(n+4)

print(f(20) + f(25))