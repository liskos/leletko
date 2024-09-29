import itertools
b = set()
for a in itertools.product("самокат", repeat=7):
    s = "".join(a)
    d = s[0]
    if s.count("сам") == 1 and ("асама" in s or "осамо" in s):
        b.add(a)
        print(a)
print(len(b))