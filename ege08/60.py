import itertools
z = set()
for a in itertools.product("абвгэюя", repeat=5):
    s = "".join(a)
    if a[0] in "эюя" and a[-1] in "эюя" and (a[1] not in "эюя" and a[2] not in "эюя" and a[3] not in "эюя" ):
        z.add(a)
print(len(z))