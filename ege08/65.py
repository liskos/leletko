import itertools
z = set()
for a in itertools.product("абвгдя", repeat=5):
    s = "".join(a)
    if (a[0] == "я" or a[-1] == "я") and s.count("я") == 1:
        z.add(a)
print(len(z))