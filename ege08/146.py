import itertools
b = 0
for a in itertools.product("размах", repeat=6):
    s = "".join(a)
    if s.count("р") + s.count("з") + s.count("м") + s.count("х") >= 3:
        b = b + 1

print(b)