import itertools
b = 0
for a in itertools.product("1234", repeat=4):
    s = "".join(a)
    if s[0] != "1" and (s[1] != s[2]):
        b = b + 1

print(b)