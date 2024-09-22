import itertools
b = set()
for a in itertools.product("инфа", repeat=6):
    s = "".join(a)
    if s.count("ф") == 2:
        b.add(s)
print(len(b))