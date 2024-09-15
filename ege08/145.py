import itertools
b = 0
for a in itertools.product("радуга", repeat=6):
    s = "".join(a)
    if s.count("р") + s.count("д") + s.count("г") >= 3:
        b = b + 1

print(b)