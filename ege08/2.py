import itertools

for i, a in enumerate(itertools.product("аоу", repeat=5), 1):
    if i == 125:
        print(i, "".join(a))