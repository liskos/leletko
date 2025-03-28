import functools
@functools.lru_cache(None)
def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 3 == 0:
        return f(n / 3) - 1
    if n >= 2 and n % 3 != 0:
        return f(n - 1) + 7

a = set()
for i in range(1, 100001):
    if f(i) == 35:
        a.add(i)
print(len(a))