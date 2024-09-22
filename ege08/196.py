import itertools
z = set()
for i in range(3, 10):
    for a in itertools.product("крыша", repeat=i):
        if ("к" not in a[1:]) and ("р" not in a[1:]) and ("ш" not in a[1:]) and (a.count("ы") <= 2) and (a.count("а") <= 2):
            z.add(a)
print(len(z))