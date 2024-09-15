import itertools
z = set()
for a in itertools.product("лето", repeat=5):
    if "".join(a).count("е") >= 1:
        z.add(a)
print(len(z))