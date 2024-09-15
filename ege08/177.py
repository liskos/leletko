import itertools
b = 0
for a in itertools.product("джобс", repeat=6):
    s = "".join(a)
    if s.count("д") == 1 and s.count("о") and s.count("с") and s.count("ж") <= 2:
        b += 1
print(b)
