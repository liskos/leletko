import functools
@functools.cache
def f(n):
    if n <= 3:
        return n - 1
    if n > 3 and n % 2 == 0:
        return f(n - 2) + n // 2 - f(n - 4)
    if n > 3 and n % 2 != 0:
        return f(n - 1) * n + f(n - 2)
for i in range(1, 5000):
    f(i)
print(f(4952) + 2 * f(4958) + f(4964))