import itertools
b = set()
for a in itertools.product("март", repeat=6):
    if "".join(a).count("р") == 2:
        b.add("".join(a))

print(len(b))