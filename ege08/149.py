import itertools
b = 0
for a in itertools.product("канкан", repeat=6):
    s = "".join(a)
    if s.count("к") + s.count("н") >= 3:
        b = b + 1

print(b)