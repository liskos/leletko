import itertools
z = set()
for a in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=3):
    z.add(a)
print(len(z))
print(26**3)