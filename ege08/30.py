import itertools
b = set()
for a in itertools.product("год",repeat=6):
    if (a[0] in "гд" ) and (a[-1] in "гд"):
        b.add(a)
print(len(b))