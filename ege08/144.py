import itertools
b = 0
for a in itertools.product("азимут", repeat=6):
    s = "".join(a)
    if s.count("з") + s.count("м") + s.count("т") >= 3:
        b = b + 1

print(b)