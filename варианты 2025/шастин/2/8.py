import itertools

b = 0
for a in itertools.product("люстра", repeat=5):
    s = "".join(a)
    d = "лстр"
    if s.count("ю") <= 2 and s[-1] not in d:
        b += 1
print(b)