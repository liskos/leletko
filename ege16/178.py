def f(n):
    if n > 2000000:
        return n
    if n <= 2000000:
        return 7 * n + f(3 * n)

def g(n):
    return f(n) / n

b = g(12345)
a = 0
for i in range(1, 1000000):
    if g(i) == b:
        a = a + 1
print(a)