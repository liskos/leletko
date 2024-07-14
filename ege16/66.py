def f(n):
    if n <= 15:
        return n * n + 11
    if n > 15 and n % 2 == 0:
        return f(n // 2) + n * n * n - 5 * n
    if n > 15 and n % 2 != 0:
        return f(n - 1) + 2 * n + 3


b = 0
for i in range(1, 1001):
    c = str(f(i))
    if c.count("6") >= 3:
        b = b + 1

print(b)