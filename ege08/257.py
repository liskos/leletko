import itertools
b = set()
for i, a in enumerate(itertools.product("аепстух", repeat=4), 1):
    s = "".join(a)
    if i > 1000 and s[0] != s[1] != s[2] != s[3]:
        print(a)
        b.add(a)
print(len(b))