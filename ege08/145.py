import itertools
b = set()
for a in itertools.product("радуга", repeat=6):
    s = "".join(a)
    if s.count("р") + s.count("д") + s.count("г") >= 3:
        b.add(a)

print(len(b))