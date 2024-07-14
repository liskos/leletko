import sys
sys.setrecursionlimit(10000)
def f(n):
    if n > 25:
        return 2 * n * n * n + 1
    if n <= 25:
        return  f(n + 2) + 2 * f(n + 3)


a = 0
for i in range(1, 1001):
    if f(i) % 11 == 0:
        a = a + 1
print(a)