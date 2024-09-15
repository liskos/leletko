import itertools
z = set()
for a in itertools.product("балкон", repeat=5):
    if "".join(a).count("б") >= 1:
        z.add(a)
print(len(z))