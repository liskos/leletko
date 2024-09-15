import itertools
b = 0
for a in itertools.product("берклий", repeat=4):
    s = "".join(a)
    if s[0] != "й" and (s.count("и") + s.count("е") >= 1):
        b = b + 1

print(b)