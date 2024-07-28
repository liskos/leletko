def s(n):
    a =  0
    while n > 0:
        a = a + n % 10
        n = n // 10
    return a



import functools
@functools.lru_cache(None)
def f(n):
    if n < 10:
        return n
    if n >= 10:
        return n % 10 + f(n // 10)


def g(n):
    if n < 10:
        return n
    if n >= 10:
        return  g(f(n))

c = 0
for i in range(10, 100):
    c =c +  s(g(i))
print(c)



