import itertools

for i, a in enumerate(itertools.product("акру", repeat=5), 1):
    if a[0] == "у":
        print(i)
        break