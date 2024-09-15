import itertools
z = set()
for a in itertools.product("абвгдя", repeat=3):
    s = "".join(a)
    if ("я" not in s[1:-1]) and s.count("я") <= 1:
        z.add(a)
print(len(z))