import itertools
b = 0
for a in itertools.product("ваяющиц", repeat=4):
    s = "".join(a)
    if s[0] != "й" and (s.count("а") + s.count("и") + s.count("я") >= 1):
        b = b + 1

print(b)