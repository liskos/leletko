import itertools
z = set()
for i, a in enumerate(itertools.product("агилморт", repeat=4), 1):
    s = "".join(a)
    if s[-1] == "л" and s[-2] == "а":
        print(i)
