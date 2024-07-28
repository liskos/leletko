import sys
sys.setrecursionlimit(10000)
import functools
@functools.lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n > 0:
        return f(n - 1) + 5 * n

a = 0
for i in range( 189456678, 567654321):
    if f(i) % 7 != 0:
        a = a + 1
print(a)