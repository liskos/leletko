import itertools
z = set()
for i, a in enumerate(itertools.product("агилмор", repeat=4), 1):
    s = "".join(a)
    if s[-1] == "м" and s[-2] == "и":
        print(i)
