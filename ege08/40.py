import itertools
z = set()
for a in itertools.product("abcx", repeat=5):
    if "x" not in a[:-1]:
        z.add(a)
print(len(z))