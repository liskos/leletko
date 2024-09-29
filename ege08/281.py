import itertools
b = 0
for a in itertools.product("11111122222222222222222222", repeat=5):
    s = "".join(a)
    if s.count("1") >= 1:
        b += s.count("1")
print(b)