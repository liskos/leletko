import itertools
b = 0
for i, a in enumerate(itertools.product("аклош", repeat=5), 1):
    s = "".join(a)
    if (s.count("о") + s.count("a")) > 0:
        b += 1
print(b)
