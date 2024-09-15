import itertools
z = set()
for i, a in enumerate(itertools.product("еикнуч", repeat=3), 1):
    s = "".join(a)
    if s[0] == "к":
        print(i)
        break