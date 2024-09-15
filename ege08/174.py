import itertools
b = 0
for a in itertools.product("калий", repeat=6):
    s = "".join(a)
    if s.count("й") <= 1 and s[0] != "й" and s[-1] != "й" and "ий" not in s and "йи" not in s:
        b += 1
print(b)
