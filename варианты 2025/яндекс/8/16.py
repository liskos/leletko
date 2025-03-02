import sys
sys.setrecursionlimit(10000)
from functools import lru_cache
@lru_cache()

def f(n):
    if n == 1:
        return 2
    if n > 1 and f(n-1) < 7555444:
        return f(n-1)+6
    else:
        f(n-1) - 7555444

print(f(10000))