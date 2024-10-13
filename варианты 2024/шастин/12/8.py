import itertools

for i, a in enumerate(itertools.product("абилмсуця", repeat=5), 1):
    s = "".join(a)
    if s.count("а") + s.count("и") + s.count("у") + s.count("я") == 2 and s[-1] != "я":
        print(i)
