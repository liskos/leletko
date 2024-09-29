import itertools

b = 0
for a in itertools.product("123456789abc0", repeat=8):
    s = "".join(a)
    if s[0] == "0":
        break
    if len(set(s)) == 6 and s.count("a") <= 2 and s[0] != "0":
        b += 1
        print(s)
print(b)