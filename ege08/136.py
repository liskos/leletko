import itertools
b = 0
for a in itertools.product("герой", repeat=4):
    s = "".join(a)
    if s[0] != "й" and s.count("е") + s.count("о") >= 1:
        b = b + 1

print(b)