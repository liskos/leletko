import itertools
z = set()
for a in itertools.product("катер", repeat=3):
    if "".join(a).count("р") >= 2:
        z.add(a)
print(len(z))