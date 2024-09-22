import itertools
b = 1
for i, a in enumerate(itertools.product("аимир", repeat=8), 1):
    s = "".join(a)
    p = s[0:4]
    k = s[4:]
    if ("м" in p and "а" in p and "р" in  p and "и" in p) and ("м" not in k and "р" not in k ):
        b += 1
        if s == "марианна":
            print(b + 1)
    print(s)
