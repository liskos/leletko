import itertools
b = set()
for a in itertools.product("кот", repeat=5):
    if "".join(a).count("о") == 2 :
        b.add("".join(a))

print(len(b))