import itertools
b = 0
for a in itertools.product("012121", repeat=5):
    s = "".join(a)
    if "11" not in s and "22" not in s and s[0] != "0" and "02" not in s and "20" not in s:
        b += 1
print(b)