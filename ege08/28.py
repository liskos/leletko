import itertools
b = set()
for a in itertools.product("крант", repeat=5):
    if "".join(a).count("к") == 2:
        b.add("".join(a))

print(len(b))