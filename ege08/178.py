import itertools
b = 0
for a in itertools.product("аклош", repeat=5):
    s = "".join(a)
    if (s.count("о") + s.count("а")) > 0:
        b += 1
print(b)
