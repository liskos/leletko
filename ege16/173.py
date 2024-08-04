def f(n):
    if n < 10:
        return n
    if n >= 10:
        return f(g(n))

def g(n):
    if n < 10:
        return f(n)
    if n >= 10:
        return g(n % 10) + g(n // 10 )

a = 0
for i in range(100, 201):
    if f(i) == 3:
        a = a + 1
print(a)