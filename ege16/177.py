def f(n):
    if n > 1000000:
        return n
    if n <= 1000000:
        return 3 * n + f(5 * n)

def g(n):
    return f(n) / n

b = g(3000)
a = 0
for i in range(1, 1000000):
    if g(i) == b:
        a = a + 1
print(a)