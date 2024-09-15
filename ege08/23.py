import itertools
b = set()
for a in itertools.product("кот", repeat=6):
    if "".join(a).count("к") == 2:
        b.add("".join(a))

print(len(b))