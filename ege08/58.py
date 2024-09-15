import itertools
z = set()
for a in itertools.product("пирог", repeat=4):
    s = "".join(a)
    if "".join(a).count("о") <= 2 and ("по" in s or "ро" in s or "го" in s):
        z.add(a)
print(len(z))