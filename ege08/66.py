import itertools
z = set()
for a in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=4):
    s = "".join(a)
    if s == s[::-1]:
        z.add(a)
print(len(z))