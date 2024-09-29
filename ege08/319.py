import itertools
b = 0
for a in itertools.product("00000000000000000000111111", repeat=10):
    s = "".join(a)
    d = "".join(sorted(s))
    if s.count("1") >= 2:
        b += 1
print(b)