import itertools
z = set()
for i, a in enumerate(itertools.product("авгдинор", repeat=4), 1):
    s = "".join(a)
    if s[0] == "и" and s[1] == "р":
        print(i)
        break