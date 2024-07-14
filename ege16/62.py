def f(n):
    if n <= 15:
        return 2 * n * n + 4 * n + 3
    if n > 15 and n % 3 == 0:
        return f(n - 1) + n * n + 3
    if n > 15 and n % 3 != 0:
        return f(n - 2) + n - 6


b = 0
for i in range(1, 1001):
    if f(i) % 2 == 1:
        b = b + 1

print(b)