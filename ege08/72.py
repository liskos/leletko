import itertools
z = set()
for i, a in enumerate(itertools.product("аклош", repeat=4), 1):
    s = "".join(a)
    if s[0] == "о":
        print(i)
        break
        