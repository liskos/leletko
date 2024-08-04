import sys
sys.setrecursionlimit(1000000000)
def f(a, b):
    if b == 0:
        return a
    if a >= b > 0:
        return f(a - b, b)
    if a < b:
        return f(b, a)

a = 0
for i in range(100000000, 200000000):
    if f(i, 15) == 3:
        a = a + 1
print(a)