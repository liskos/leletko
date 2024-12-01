import itertools

for i, a in enumerate(itertools.product("дикмо", repeat=5), 1):
    s = "".join(a)
    if "мм" not in s and s.count("м") == 2:
        print(i)
