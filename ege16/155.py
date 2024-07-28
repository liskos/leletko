import sys
sys.setrecursionlimit(10000)
import functools
@functools.lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n > 0:
        return f(n - 1) + 3 * n

a = 0
for i in range(123456789,213789654):
    if f(i) % 5 != 0:
        a = a + 1
print(a)
