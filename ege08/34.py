import itertools

for i, a in enumerate(itertools.product("азнс", repeat=5), 1):
    if "".join(a) == "сазан" or "".join(a) == "занас":
        print(i)