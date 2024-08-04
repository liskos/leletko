import sys
sys.setrecursionlimit(10000)
import functools
@functools.lru_cache(None)
def f(n):
    if n >= 2025:
        return n
    if n < 2025:
        return f(n + 1) - f(n + 2) + 7

print(f(15) - f(24))