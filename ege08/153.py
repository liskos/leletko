import itertools
b = 0
for a in itertools.product("1234", repeat=5):
    s = "".join(a)
    if s[0] != "1" and s[0] != s[4] and s[1] != s[3]:
        b = b + 1

print(b)