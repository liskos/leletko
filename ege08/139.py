import itertools
b = 0
for a in itertools.product("енисй", repeat=4):
    s = "".join(a)
    if s[0] != "й" and (s.count("е") + s.count("и") >= 1):
        b = b + 1

print(b)