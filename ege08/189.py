import itertools
b = 0
for a in itertools.product("корнет", repeat=5):
    s = "".join(a)
    if s.count("о") <= 1 and s.count("е") <= 1:
        b += 1
print(b)