import itertools
b = set()
for a in itertools.product("кант", repeat=6):
    if "".join(a).count("к") == 2:
        b.add("".join(a))

print(len(b))