import itertools

for i, a in enumerate(itertools.product("wsda", repeat=5),1):
    s = "".join(a)
    if "dd" in s and s[-1] != "w" and s.count("s") >= 1:
        print(i)
        break