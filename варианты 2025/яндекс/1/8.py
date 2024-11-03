import itertools

for i, a in enumerate(itertools.product("бикнопр", repeat=6), 1):
    s = "".join(a)
    if "ооо" in s and len(set(s)) == 4 and s.count("о") == 3:
        print(i)