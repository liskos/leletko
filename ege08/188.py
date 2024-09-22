import itertools
b = 0
for a in itertools.product("сакура", repeat=5):
    s = "".join(a)
    if s.count("а") <= 1 and s.count("у") <= 1:
        b += 1
print(b)