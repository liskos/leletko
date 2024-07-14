import functools
@functools.lru_cache(None)
def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 8 == 0:
        return n + f(n / 2 - 3)
    if n > 5 and n % 8 != 0:
        return 1

a = set()
for i in range(1, 100000):
    a.add(f(i))
print(max(a))
