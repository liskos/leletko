import itertools
z = set()
for i, a in enumerate(itertools.product("авген", repeat=4), 1):
    s = "".join(a)
    if s.count("а") == 0:
        print(i)
        break