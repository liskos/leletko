import itertools
b = 0
for a in itertools.product("аимнр", repeat=8):
    s = "".join(a)
    p = s[0:4]
    k = s[4:]
    if ("м" in p and "а" in p and "р" in p and "и" in p) and (set(k) <= {"и","н","а"} ):
        b += 1
        if s == "марианна":
            print(b)
