
import sys
sys.setrecursionlimit(10000)
import functools
@functools.lru_cache(None)
def f(n):
    if n < 10:
        return n
    if n >= 10:
        return (n % 10) * f(n // 10)
a = 0
for i in range(1000000000000, 9999999999999):
    if f(i) != 0:
        a = a + 1
print(a)