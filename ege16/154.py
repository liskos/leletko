import sys
sys.setrecursionlimit(10000)
import functools
@functools.lru_cache(None)
def f(n):
    if n == 0:
        return 0
    else:
        return f(n - 1) + 2 * n

a = 0
for i in range(100000000, 200000000):
    if f(i) % 3 != 0:
        a = a + 1
print(a)
