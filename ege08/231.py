import itertools
b = set()
for a in itertools.product("012345678", repeat=7):
    s = "".join(a)
    if s[0] != "0" and s[-1]not in "347":
        if all(len(set(a[i:i+3]))!=1 for i in range(7-2)):
            b.add(s)
print(len(b))