def f(n):
    if n > 1000000:
        return n
    if n <= 1000000:
        return n + f(4 * n)

def g(n):
    return f(n) / n

b = g(2000)
a = 0
for i in range(1, 1000000):
    if g(i) == b:
        a = a + 1
print(a)