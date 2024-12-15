import itertools

for i, a in enumerate(itertools.product("аикмнортф", repeat=6), 1):
    s = "".join(a)
    if s.count("и") == 0 and s.count("р") == 3 and s[0] != "а":
        print(i)
        break