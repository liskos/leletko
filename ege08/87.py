import itertools
z = set()
for i, a in enumerate(itertools.product("векно", repeat=5), 1):
    s = "".join(a)
    if s.count("н") == 2 and s.count("к") == 2:
        print(i)
