import itertools
z = set()
for a in itertools.product("слон", repeat=5):
    if "".join(a).count("о") <= 3:
        z.add(a)
print(len(z))