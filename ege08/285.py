import itertools
b = set()
for a in itertools.product("0123456789ab", repeat=6):
    s = "".join(a)
    d = s[0]
    if s[0] != "0" and int(s, 12) % int(d, 12) == 0:
        b.add(a)
        print(a)
print(len(b))
