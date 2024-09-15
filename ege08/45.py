import itertools
z = set()
for a in itertools.product("клоун", repeat=5):
    if "".join(a).count("у") >= 1:
        z.add(a)
print(len(z))