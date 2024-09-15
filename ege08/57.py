import itertools
z = set()
for a in itertools.product("пирог", repeat=6):
    s = "".join(a)
    if "".join(a).count("р") == 1 and ("ри" in s or "ро" in s):
        z.add(a)
print(len(z))