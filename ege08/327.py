import itertools
b = 0
for a in itertools.product("01010", repeat=6):
    s = "".join(a)
    if s.count("1") > s.count("0"):
        b += 1
        print(s)
print(b)
