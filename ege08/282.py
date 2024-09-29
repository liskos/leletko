import itertools
b = 0
for a in itertools.product("0123456789", repeat=7):
    s = "".join(a)
    if s[0] == "2" and s[1] == "4" and s[1] == s[2] and s[-1] and s[0] != "0":
        b += 1
print(b)