import itertools
b = 0
for a in itertools.product("рустам", repeat=6):
    s = "".join(a)
    if s.count("р") + s.count("с") + s.count("т") + s.count("м") >= 3:
        b = b + 1

print(b)