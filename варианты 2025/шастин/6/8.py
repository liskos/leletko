import itertools

o = 0
for k in range(1, 20):
    d = 0
    for i in itertools.product("01", repeat=20):
        s = "".join(i)
        if s.count("0") == k:
            d += 1
    if d >= 100000 and d <= 999999:
        o = d

print(o)