import itertools
b = set()
for a in itertools.product("кума", repeat=5):
    if (a[0] in "км" ) and (a[-1] in "уа"):
        b.add("".join(a))

print(len(b))