import itertools

for i, a in enumerate(itertools.product("бенрстья", repeat=5), 1):
    s = "".join(a)
    if s[0] == "р" and s.count("ь") == 0:
        print(i)