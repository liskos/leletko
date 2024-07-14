import sys
sys.setrecursionlimit(1000000)
def f(n):
    if n < 3:
        return n + 1
    if n >= 3 and n % 2 == 0:
        return f(n - 2) + n - 2
    if n >= 3 and n % 2 == 1:
        return 0

b = 0
for i in range(1, 10000):
    c = f(i)
    if len(str(c)) == 5:
        b = b + 1

print(b)