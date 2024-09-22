import itertools
b = set()
for a in itertools.product("пикачу", repeat=5):
    s = "".join(a)
    if s.count("у") >= 2:
        b.add(s)
print(len(b))