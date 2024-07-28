import sys
sys.setrecursionlimit(10000)
import functools
@functools.lru_cache(None)
def f(n):
    if n < 10:
        return 0
    else:
        return f(n // 10 ) + (n // 10 % 10) - ( n % 10)


a = 0
for i in range(1, 1000000001):
    if f(i) == 9:
        a = a + 1
print(a)