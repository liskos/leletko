import itertools
b = set()
for i, a in enumerate(itertools.product("аежйму", repeat=5), 1):
    s = "".join(a)
    if i % 2 == 0 and s[0] != s[1] != s[2] != s[3] != s[4]:
        b.add(s)
        print(a)
print(len(b))
