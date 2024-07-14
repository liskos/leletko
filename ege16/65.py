def f(n):
    if n <= 5:
        return n + 15
    if n > 5 and n % 2 == 0:
        return f(n // 2) + n * n * n - 1
    if n > 5 and n % 2 != 0:
        return f(n - 1) + 2 * n * n + 1


b = 0
for i in range(1, 1001):
    c = str(f(i))
    if c.count("8") >= 2:
        b = b + 1

print(b)