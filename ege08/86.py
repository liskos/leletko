import itertools
z = set()
for i, a in enumerate(itertools.product("векно", repeat=5), 1):
    s = "".join(a)
    if s.count("о") == 1 and s.count("е") == 1:
        print(i)
