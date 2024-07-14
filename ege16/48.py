import functools
@functools.lru_cache(None)
def f(n):
    if n <= 3:
        return n
    if n > 3 and n % 2 == 0:
        return n + f(n -1)
    if n > 3 and n % 2 == 1:
        return n * n + f(n - 2)

a = 0
for i in range(1, 100000):
    if f(i) < 10 ** 8:
        a = a + 1
print(a)