import itertools
b = set()
for a in itertools.product("012345678", repeat=7):
    s = "".join(a)
    if s[0] != "0" and s[0] != "3" and s[0] != "7":
        if s[0] != s[1] != s[2] != s[3] != s[4] != s[5] != s[6]:
            b.add(s)
print(len(b))
