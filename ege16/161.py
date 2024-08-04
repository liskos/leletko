def f(n):
    if n < 10:
        return  n
    if 10 <= n < 1000:
        return f(n // 10) + f(n % 10)
    if n >= 1000:
        return f(n // 1000) - f(n % 1000)

a = 0
for i in range(1, 10 ** 6):
    if f(i) == 0:
        a = a + 1
print(a)