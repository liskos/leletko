import itertools

k = 0
for a in itertools.product("0123456", repeat=6):
    s = "".join(a)
    if s[0] != "0" and s.count("0") == 1 and ((s.count("0") + s.count("2") + s.count("4") + s.count("6")) % 2 == 0):
        k += 1

print(k)