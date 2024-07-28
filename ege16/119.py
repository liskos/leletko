import functools
@functools.lru_cache(None)
def f(n):
    if n == 0:
        return 1
    if n > 0 and n % 2 != 0:
        return 1 + f(n - 1)
    else:
        return  f(n / 2)


a = 0
for i in range(1, 500000000):
    if f(i)  == 5:
        a = a + 1
        print(i)
print(a)