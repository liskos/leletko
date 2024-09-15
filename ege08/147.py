import itertools
b = 0
for a in itertools.product("кортик", repeat=6):
    s = "".join(a)
    if s.count("к") + s.count("р") + s.count("т") >= 3:
        b = b + 1

print(b)