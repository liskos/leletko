import functools
@functools.lru_cache(None)
def f(n, m):
    if m== 0:
        return 10**7
    if n <= 5:
        return n
    if n > 10 ** 6:
        return  10 ** 7
    if n > 5 and n % 5 == 0:
        return n + f(n // 5 + 1, m - 1)
    if n > 5 and n % 5 != 0:
        return n + f(n + 6, m - 1)

for i in range(1, 100000):
    if 1000 <f(i, 100) <10 ** 7:
        print(i, f(i, 100))
        break
