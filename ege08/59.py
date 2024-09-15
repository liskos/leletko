import itertools
z = set()
for a in itertools.product("пирог", repeat=5):
    s = "".join(a)
    ss = s.replace("ри", "**").replace("ро", "**")
    if "".join(a).count("р") <= 2 and "р" not in ss:
        z.add(a)
print(len(z))