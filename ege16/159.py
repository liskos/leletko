import functools
@functools.lru_cache(None)
def f(a, b):
    if a == 0 and b == 0:
        return 0
    if a > b:
        return f(a - 1, b) + b
    if a <= b:
        return f(a, b - 1) + a

c = set()

for a in range(1, 100):
    for b in range(1, 100000000):
        if f(a, b) == 18522000:
            print(a, b, a*b)
print(len(c))
