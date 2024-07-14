def s(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

import sys
sys.setrecursionlimit(10000)
def f(n):
    if n > 30:
        return n * n + 5 * n + 4
    if n <= 30 and n % 2 == 0:
        return 2 * f(n + 1) + f(n + 4)
    if n <= 30 and n % 2 == 1:
        return f(n + 2) + 3 * f(n + 5)


b = 0
for i in range(1, 1001):
    d = f(i)
    if s(d) == 27:
        b = b + 1

print(b)