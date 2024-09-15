import itertools
z = set()
for a in itertools.product("сироп", repeat=5):
    s = "".join(a)
    if "".join(a).count("о") == 1 and ("со" in s or "ро" in s or "по" in s):
        z.add(a)
print(len(z))