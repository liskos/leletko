import itertools

z = set()
for i, a in enumerate(itertools.product("артф", repeat=5), 1):
    s = "".join(a)
    if s[0] == "т":
        print(i)
        break
