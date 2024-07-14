import functools
@functools.lru_cache(None)
def f(n):
    if n <= 1:
        return n
    if n > 1 and n % 3 == 0:
        return n + f(n / 3 - 1)
    if n > 1 and n % 3 != 0:
        return 1

for i in range(1, 100000):
    if f(i) > 1000:
        print(i)
        break
print(f(2))