import itertools
b = 0
for a in itertools.product("123456789abcdef", repeat=5):
    s = "".join(a)
    if "".join(sorted(s)) == s:
        b += 1
        print(s)
print(b)