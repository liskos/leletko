import itertools
b = 0
for a in itertools.product("джобс", repeat=6):
    s = "".join(a)
    if s.count("д") == 1 and s.count("о")==1 and s.count("с")==1 and s.count("ж") <= 2:
        b += 1
print(b)
