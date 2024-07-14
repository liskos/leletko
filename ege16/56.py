import sys
sys.setrecursionlimit(10000)
def f(n):
    if n > 20:
        return n * n * n + n
    if n <= 20 and n % 2 == 0:
        return 3 * f(n + 1) + f(n + 3)
    if n <= 20 and n % 2 == 1:
        return f(n + 2) + 2 * f(n + 3)


a = 0
for i in range(1, 1001):
    if "1" not in str(f(i)):
        a = a + 1
print(a)