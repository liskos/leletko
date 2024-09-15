import itertools
b = 0
for i, a in enumerate(itertools.product("авдпр", repeat=4), 1):
    s = "".join(a)
    if s.count("а") == 0 and s.count("в") == 1 and s.count("д") == 1 and s.count("п") == 1 and s.count("р") == 1:
        print(i)
print(b)
