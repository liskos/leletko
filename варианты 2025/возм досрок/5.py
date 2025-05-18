def g(n):
    b = ""
    while n > 0:
        b = b + str(n%3)
        n = n // 3
    return b[::-1]


def f(n):
    b = g(n)
    if n % 3 == 0:
        b = b + b[:3]
    else:
        b = b + g(sum([int(x) for x in b]))
    return int(b,3)

r = []
print(f(10))
for i in range(1,1000):
    if f(i) % 2 == 1 and f(i) > 2500:
        r.append(f(i))

print(min(r))