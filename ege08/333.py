import itertools

b = 0
for a in itertools.product("01232527292b2d2f", repeat=8):
    s = "".join(a)
    if s.count("0") + s.count("2") == 3 and s[0] != "0":
        b += 1
        print(s)
print(b)