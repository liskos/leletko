import sys
sys.setrecursionlimit(10000)
import functools
@functools.lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n > 0:
        return f(n // 10 ) + ( n % 10)

a = 0
for i in range(865432015, 1585342628):
    if f(i) > f(i + 1):
        a = a + 1
print(a)