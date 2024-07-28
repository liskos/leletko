import functools
@functools.lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n / 2) - 2
    if n > 0 and n % 2 != 0:
        return 2 + f(n - 1)

a = 0
for i in range(1, 1000):
     if f(i) == -2:
         a = a + 1
print(a)
