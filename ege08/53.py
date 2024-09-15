import itertools
z = set()
for a in itertools.product("муха", repeat=5):
    if "".join(a).count("у") <= 3:
        z.add(a)
print(len(z))