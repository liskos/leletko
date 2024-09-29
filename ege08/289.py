import itertools
b = 0
for a in itertools.product("1010ш0111", repeat=4):
    s = "".join(a)
    if s[0] != "0" and s[0] != "ш":
        b += 1
        print(a)
print(b)