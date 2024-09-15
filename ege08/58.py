import itertools
z = set()
for a in itertools.product("пирог", repeat=4):
    s = "".join(a)
    ss = s.replace("по", "**")
    ss = ss.replace("ро", "**")
    ss = ss.replace("го", "**")
    if "".join(a).count("о") <= 2 and "о" not in ss:
        z.add(a)
print(len(z))