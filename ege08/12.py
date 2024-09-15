import itertools

for i, a in enumerate(itertools.product("аоу", repeat=5), 1):
    if a[0] == "о":
        print(i)
        break