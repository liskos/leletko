import itertools

z = set()
for i, a in enumerate(itertools.product("адр", repeat=6), 1):
    s = "".join(a)
    if s[0] == "р":
        print(i)
        break
