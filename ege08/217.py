import itertools
b = set()
for a in itertools.product("чоаниме", repeat=6):
    s = "".join(a)
    if s.count("м") == 3:
        b.add(s)
print(len(b))
print(24+ 360 + 4320)