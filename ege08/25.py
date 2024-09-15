import itertools
b = set()
for a in itertools.product("ток", repeat=6):
    if "".join(a)[0] == "т" or "".join(a)[0] == "к":
        b.add("".join(a))

print(len(b))