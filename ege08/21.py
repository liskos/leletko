import itertools
b = set()
for a in itertools.product("лето", repeat=4):
    if "".join(a)[0] == "л" or "".join(a)[0] == "т":
        b.add("".join(a))

print(len(b))