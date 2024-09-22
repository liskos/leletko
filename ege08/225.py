import itertools
b = set()
for a in itertools.product("01234", repeat=5):
    s = "".join(a)
    if (s.count("0") + s.count("2") + s.count("4") <= 3) and s[0] != "0":
        b.add(s)
        print(s)
print(len(b))
