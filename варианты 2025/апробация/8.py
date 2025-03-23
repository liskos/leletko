import itertools

for i,a in enumerate(itertools.product("косуф", repeat=5), 1):
    s = "".join(a)
    if s.count("ф") == 0 and s.count("у") == 2:
        print(i)