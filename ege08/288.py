import itertools
b = 0
for a in itertools.product("1010ш0111", repeat=4):
    s = "".join(a)
    if s.count("1") + s.count("ш") == s.count("0") and "0ш" not in s and "ш0" not in s:
        b += 1
        print(a)
print(b)