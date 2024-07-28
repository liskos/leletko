import functools
@functools.lru_cache(None)
def f(n):
    if n == 0:
        return 8
    if n > 0 and n % 3 == 0:
        return 5 + f(n // 3)
    else:
        return  f(n // 3)


a = 0
for i in range(1, 500000000):
    if f(i)  == 3:
        a = a + 1
        print(i)
print(a)