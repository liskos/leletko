import itertools
z = set()
for i in range(3, 10):
    for a in itertools.product("сепия", repeat=i):
        if ("с" not in a[1:]) and ("п" not in a[1:]) and (a.count("и") <= 2) and (a.count("е") <= 2) and (a.count("я") <= 2):
            z.add(a)
print(len(z))