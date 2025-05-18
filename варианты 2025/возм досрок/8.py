import itertools

for i, a in enumerate(itertools.product("АКМС", repeat=6), 1):
    s = "".join(a)
    if s.count("С") == 0 and s.count("М") == 0 and "КК" not in s:
        print(i)