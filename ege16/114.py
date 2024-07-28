import functools
@functools.lru_cache(None)
def f(n):
    if n == 0:
        return 1
    if n > 0:
        return  7 * (n - 1) + f(n - 1)

def pr():
    a = [2]
    for i in range(3, 140000):
        for j in a:
            if i % j == 0:
                break
        else:
            a.append(i)
    return a

p = pr()
a = 0
for i in range(2, 201):
    if f(i) in p:
        a += 1
print(a)
