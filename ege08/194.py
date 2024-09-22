import itertools
z = set()
for i in range(3, 10):
    for a in itertools.product("лида", repeat=i):
        if ("л" not in a[1:]) and ("д" not in a[1:]) and (a.count("и") <= 2) and (a.count("а") <= 2):
            z.add(a)
print(len(z))