import itertools
b = set()
for a in itertools.product("polygon", repeat=5):
    s = "".join(a)
    if s == s[::-1] and s[2] == "o":
        b.add(a)
        print(a)
print(len(b))