import itertools

b = 0
for a in itertools.product("люстра", repeat=5):
    s = "".join(a)
    if s.count("ю") <= 2 and s[-1] in "аю":
        b += 1
print(b)