import itertools
b = set()
for a in itertools.product("обществ", repeat=5):
    s = "".join(a)
    if s[0] not in "щб" and s[-2:] == "вв" and "ев" not in s and "ве" not in s and "тб" in s:
        b.add(a)
        print(a)
print(len(b))
