import itertools
b = set()
for a in itertools.product("012345678", repeat=7):
    s = "".join(a)
    if s[0] != "0" and s[0] != "3" and s[0] != "7":
        if all(a[i] != a[i+1] for i in range(7-1)):
            b.add(s)
print(len(b))
