import functools
@functools.lru_cache(None)
def f(n):
    if n == 0:
        return 1
    if n > 0:
        return  7 * (n - 1) + f(n - 1)

a = 0
for i in range(2, 201):
     if f(i) == 0:
         a = a + 1
print(a)
