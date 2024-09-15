import itertools
z = set()
for i, a in enumerate(itertools.product("аиоуэ", repeat=4), 1):
    s = "".join(a)
    if s == "иааэ":
        print(i)
