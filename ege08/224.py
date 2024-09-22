import itertools
b = set()
for a in itertools.product("01234567", repeat=4):
    s = "".join(a)
    d = "".join(sorted(s))
    if int(s[0]) % 2 == 0 and d[::-1] == s:
        b.add(s)
        print(s)
print(len(b))
