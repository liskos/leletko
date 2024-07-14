def s(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

import sys
sys.setrecursionlimit(10000)
def f(n):
    if n <= 15:
        return n * n + 3 * n + 9
    if n > 15 and n % 3 == 0:
        return f(n - 1) + n - 2
    if n > 15 and n % 3 != 0:
        return f(n - 2) + n + 2


b = 0
for i in range(1, 1001):
    if set(str(f(i))) <= {"0", "2", "4", "6", "8"} :
        b = b + 1

print(b)