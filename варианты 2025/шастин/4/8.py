import itertools

k = 0
for a in itertools.product("0123456789ab", repeat=6):
    s = "".join(a)
    h = s.count("2") + s.count("0") + s.count("4") + s.count("6") + s.count("8") + s.count("a")
    n = s.count("1") + s.count("3") + s.count("5") + s.count("7") + s.count("9") + s.count("b")
    if s.count("b") == 1 and h == n and s[0] != "0":
        k += 1
print(k)