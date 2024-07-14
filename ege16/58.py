import sys
sys.setrecursionlimit(10000)
def f(n):
    if n > 30:
        return n * n + 3 * n + 5
    if n <= 30 and n % 2 == 0:
        return 2 * f(n + 1) + f(n + 4)
    if n <= 30 and n % 2 == 1:
        return f(n + 2) + 3 * f(n + 5)


a = 0
for i in range(1, 1001):
    b = str(f(i))
    if b.count("0") >= 2:
        a = a + 1
        print(f(i))
print(a)