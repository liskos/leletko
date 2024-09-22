import itertools
b = 0
for a in itertools.product("0123456789", repeat=3):
    s = "".join(a)
    if "".join(sorted(s)) == s and s[0] != "0":
        b += 1
print(b)