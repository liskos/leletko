import itertools
b = 0
for a in itertools.product("льса", repeat=6):
    s = "".join(a)
    if s.count("а") <= 1:
        b += 1
print(b)