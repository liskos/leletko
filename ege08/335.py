import itertools

b = 0
for a in itertools.product("1234567890", repeat=10):
    s = "".join(a)
    if s[0] == "0":
        break
    if s.count("3") == s.count("2") and s[0] != "0":
        b += 1
        print(s)
print(b)