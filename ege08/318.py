import itertools
b = set()
for a in itertools.product("01234567", repeat=6):
    s = "".join(a)
    d = "".join(sorted(s))
    if s[0] != "0" and (s[0] == d[0] or s[0] == d[1]) and (s[1] == d[0] or s[1] == d[1]) and d[2] != d[1]:
        b.add(s)
        print(s)
print(len(b))