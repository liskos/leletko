def devided(n):
    a = set()
    r = []
    k = 0
    for i in range(1, int(n ** 0.5) + 1):
        if k >=3:
            break
        if n % i == 0:
            a.add(i)
            a.add(n // i)
            if i % 2 == 0:
                k += 1
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


print(devided(103018658))
for i in range(113000000,114000000+1):
    if i % 2 == 0 and len(devided(i)) > 0:
        print(i,sorted(devided(i))[1])