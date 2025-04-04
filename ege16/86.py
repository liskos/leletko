import functools
@functools.lru_cache(None)
def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 2 == 0:
        return f(n / 2) + 1
    if n >= 2 and n % 2 != 0:
        return f(n - 3) + 3

a = set()
for i in range(1, 100001):
    if f(i) == 12:
        a.add(i)
print(len(a))