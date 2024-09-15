import itertools
z = set()
for a in itertools.product("кран", repeat=3):
    if "".join(a).count("а") >= 1:
        z.add(a)
print(len(z))