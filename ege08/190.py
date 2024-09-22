import itertools
b = 0
for a in itertools.product("лька", repeat=5):
    s = "".join(a)
    if s.count("а") <= 1:
        b += 1
print(b)