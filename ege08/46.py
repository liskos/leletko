import itertools
z = set()
for a in itertools.product("балкон", repeat=3):
    if "".join(a).count("б") >= 1:
        z.add(a)
print(len(z))