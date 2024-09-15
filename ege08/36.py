import itertools

for i, a in enumerate(itertools.product("амрт", repeat=4), 1):
    if "".join(a) == "март" or "".join(a) == "рамт":
        print(i)