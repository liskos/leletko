import itertools

for i, a in enumerate(itertools.product("акру", repeat=5), 1):
    if i == 250:
        print(i, "".join(a))