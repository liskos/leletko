import itertools
z = set()
for a in itertools.product("слон", repeat=5):
    if 0 < a.count("о") <= 3:
        z.add(a)
print(len(z))
print(z)