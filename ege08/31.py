import itertools
b = set()
for a in itertools.product("метро", repeat=4):
    if (a[0] in "мтр" ) and (a[-1] in "ео"):
        b.add("".join(a))

print(len(b))