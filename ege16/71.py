def s(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

import sys
sys.setrecursionlimit(1000000)
def f(n):
    if n == 0:
        return 5
    if n > 0:
        return 3 * f(n - 4)
    if n < 0:
        return f(n + 3)

print(f(43))