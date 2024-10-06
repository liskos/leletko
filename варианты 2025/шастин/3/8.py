import itertools

b = 0
for i, a in enumerate(itertools.product("престол", repeat=5), 1):
    s = "".join(a)
    if i % 2 == 0 and s[0] in "ео" and s.count("е") + s.count("о") >= 2:
        b += 1
print(b)