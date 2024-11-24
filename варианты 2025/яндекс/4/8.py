import itertools

k = 0
for i in itertools.product("01212121212b", repeat=6):
    s = "".join(i)
    if s[0] != "0" and s.count("0") + s.count("2") == s.count("1") + s.count("b") and s.count("b") == 1:
        k += 1

print(k)