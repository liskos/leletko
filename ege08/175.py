import itertools
b = 0
for a in itertools.product("в", repeat=6):
    s = "".join(a)
    if s.count("й") <= 1 and s[0] != "й" and s[-1] != "й" and "ей" not in s and "йе" not in s:
        b += 1
print(b)
