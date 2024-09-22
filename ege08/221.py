import itertools
b = set()
for a in itertools.product("оникс", repeat=6):
    s = "".join(a)
    if s.count("с") == 3 and s.count("о") == 1:
        b.add(s)
print(len(b))
print(4 + 60 + 540)