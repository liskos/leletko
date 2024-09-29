import itertools
b = 0
for a in itertools.product("к1нф1т1", repeat=5):
    s = "".join(a)
    if s.count("1") >= 2 and "11" not in s:
        b += 1
        print(s)
print(b)