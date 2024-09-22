import itertools
b = 0
for a in itertools.product("банкир", repeat=6):
    s = "".join(a)
    if s.count("а") <= 1 and s.count("и") <= 1:
        b += 1
print(b)