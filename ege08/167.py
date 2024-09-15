import itertools
b = 0
for a in itertools.product("объем", repeat=4):
    s = "".join(a)
    if s.count("о") == 1 and s[0] != "ъ" and s[-1] != "ъ":
        b += 1
print(b)
