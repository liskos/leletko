import functools
@functools.lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    if n > 1 and n % 3 == 0:
        return 2 * f(n - 1) + f(n - 2)
    else:
        return 3 * f(n - 2) + f(n - 1)

def pr():
    a = [2]
    for i in range(3, 200):
        for j in a:
            if i % j == 0:
                break
        else:
            a.append(i)
    return a

p = pr()
a = 0
for i in range(1, 35+1):
    if sum(map(int, str(f(i)))) in p:
        a += 1
print(a)
