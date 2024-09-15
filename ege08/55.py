import itertools
z = set()
for a in itertools.product("жираф", repeat=6):
    if 0 < "".join(a).count("а") <= 4:
        z.add(a)
print(len(z))