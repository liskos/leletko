import itertools
b = 0
for a in itertools.product("гафний", repeat=4):
    s = "".join(a)
    if s[0] != "й" and (s.count("а") + s.count("и") >= 1):
        b = b + 1

print(b)