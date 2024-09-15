import itertools
z = set()
for a in itertools.product("абвгде", repeat=4):
    s = "".join(a)
    if s.count("г") == 1 and (s[0] == "г" or s[-1] == "г"):
        z.add(a)
print(len(z))