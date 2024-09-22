import itertools
b = 0
for a in itertools.product("12345", repeat=3):
    s = "".join(a)
    if "".join(sorted(s)) == s:
        b += 1
print(b)