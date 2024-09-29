import itertools
b = set()
for a in itertools.product("01234567", repeat=5):
    s = "".join(a)
    if s[0] != "0" and s.count("6") == 1:
        s = s.replace("3", "1").replace("5", "1").replace("7", "1")
        if "16" not in s and "61" not in s:
            b.add(a)
print(len(b))
