def f(x):
    p = 17 <= x <= 61
    q = 39 <= x <= 91
    a = a1 <= x <= a2
    return (q and not a) and (a or not p)
Ox = [i/4 for i in range(15*4, 95*4)]
res = []
for a1 in Ox:
    for a2 in Ox:
        if all(f(x) == 0 for x in Ox):
            res.append(a2-a1)

print(min(res))