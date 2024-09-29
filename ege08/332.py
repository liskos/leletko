import itertools
b = 0
for a in itertools.product("012141618", repeat=7):
    s = "".join(a)
    if s.count("8") == 1 and s.count("1") == 4 and s[0] != "0":
        b += 1
        print(s)
print(b)