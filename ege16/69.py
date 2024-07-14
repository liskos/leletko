def s(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

import sys
sys.setrecursionlimit(1000000)
def f(n):
    if n < 4:
        return n - 1
    if n >= 4 and n % 3 == 0:
        return n + 2 * f(n - 1)
    if n >= 4 and n % 3 != 0:
        return f(n - 2) + f(n - 3)

print(s(f(25)))