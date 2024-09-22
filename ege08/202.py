import itertools
b = 0
for a in itertools.product("питон", repeat=4):
    s = "".join(a)
    s = s.replace("т", "п").replace("н", "п")
    s = s.replace("о", "и")
    if "пп" not in s and "ии" not in s:
        b += 1
        print(a)
print(b)