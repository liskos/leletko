import itertools

for i, a in enumerate(itertools.product("амрт", repeat=4), 1):
    if i == 250:
        print("".join(a))
        break