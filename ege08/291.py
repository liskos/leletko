import itertools
b = 0
for a in itertools.product("1010ш0в11", repeat=5):
    s = "".join(a)
    if "вш" not in s and "шв" not in s and "0ш" not in s and "ш0" not in s:
        b += 1
        print(a)
print(b)