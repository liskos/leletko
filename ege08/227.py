import itertools
b = set()
for a in itertools.product("01234567", repeat=4):
    s = "".join(a)
    if int(s) % 4 == 0 and s[0] != "0":
        b.add(s)
print(len(b))
