def f(n):
    if n <= 13:
        return n * n * n + n * n + 1
    if n > 13 and n % 3 == 0:
        return f(n - 1) + 2 * n * n - 3
    if n > 13 and n % 3 != 0:
        return f(n - 2) + 3 * n + 6


b = 0
for i in range(1, 1001):
    if set(str(f(i))) <= {"1", "3", "5", "7", "9"}:
        b = b + 1
print(b)