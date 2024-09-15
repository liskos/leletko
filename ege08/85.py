import itertools
z = set()
for i, a in enumerate(itertools.product("аоу", repeat=5), 1):
    s = "".join(a)
    if s[2] == "у":
        print(i)
        break
