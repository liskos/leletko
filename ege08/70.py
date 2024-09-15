import itertools
z = set()
for a in itertools.product("абвг", repeat=5):
    s = "".join(a)
    if s.count("г") == 1 and (s[0] == "г" or s[-1] == "г"):
        z.add(a)
    if s.count("г") == 0:
        z.add(a)
print(len(z))