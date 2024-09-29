import itertools
b = set()
for a in itertools.product("012345678", repeat=5):
    s = "".join(a)
    if int(s[0]) % 2 == 0 and s[-1] not in "18" and s.count("3") <= 1:
        b.add(a)
print(len(b))