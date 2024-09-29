import itertools
for i, a in enumerate(itertools.product("штсмкеива", repeat=5), 1):
    s = "".join(a)
    d = s.replace("и","е").replace("а", "е")
    if s == s[::-1] and d.count("е") == 4:
        print(i)
        print(a)
        break