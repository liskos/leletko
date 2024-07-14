def f(n):
    if n <= 18:
        return n + 3
    if n > 18 and n % 3 == 0:
        return (n // 3) * f(n // 3) + n - 12
    if n > 18 and n % 3 != 0:
        return f(n - 1) + n * n + 5


b = 0
for i in range(1, 801):
    if f(i) % 2 == 0:
        b = b + 1

print(b)