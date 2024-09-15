import itertools
z = set()
for a in itertools.product("комар", repeat=4):
    if "".join(a).count("а") <= 3:
        z.add(a)
print(len(z))