import functools
@functools.lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n / 2) - 1
    if n > 0 and n % 2 != 0:
        return 3 + f(n - 1)

a = set()
for i in range(1, 1000):
     a.add(f(i))
     print(f(i))
print(len(a))
