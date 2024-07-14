import sys
sys.setrecursionlimit(10000)
def f(n):
    if n <= 3:
        return n
    if n > 3 and n % 2 == 0:
        return 2 * n * n + f(n - 1)
    if n > 3 and n % 2 == 1:
        return n * n * n + n + f(n - 1)

a = 0
for i in range(1, 1000):
    if f(i) < 10 ** 7:
        a += 1
print(a)