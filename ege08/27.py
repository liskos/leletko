import itertools
b = set()
for a in itertools.product("крот", repeat=6):
    if "".join(a).count("о") == 1:
        b.add("".join(a))

print(len(b))