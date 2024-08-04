import functools
@functools.cache
def f(n):
    if n < 9:
        return n // 3 + n % 3
    if n >= 9:
        return f(n // 9) + f(n % 9)


a = 0
for i in range(9**8, 9 ** 9):
    if f(i) == 33:
        a = a + 1
print(a)