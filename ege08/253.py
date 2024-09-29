import itertools
b = set()
for a in itertools.product("огэинф", repeat=6):
    s = "".join(a)
    if s[0] in "эо" and s[-2:] == "нф" and s.count("иг") >= 1 and "огэ" not in s:
        b.add(a)
        print(a)
print(len(b))