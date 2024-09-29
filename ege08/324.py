import itertools
b = set()
for a in itertools.product("01214161", repeat=10):
    s = "".join(a)
    if s.count("1") == 3 and "11" not in s and s[0] != "0":
        b.add(s)
        print(s)
print(len(b))
