def devided(n):
    a = set()
    r = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    d = []
    for y in a:
        if y != 1 and y != n:
            d.append(y)
    for x in a:
        if x % 2 == 0:
            r.append(x)
    if len(r) == 3:
        return d
    return []
print(devided(100224482))
for i in range(100000000,101000000+1):
    if i % 2 == 0 and len(devided(i)) > 0:
        print(i,sorted(devided(i))[1])