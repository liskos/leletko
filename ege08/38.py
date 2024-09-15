import itertools

for i, a in enumerate(itertools.product("аоу", repeat=5), 1):
    if "".join(a) == "уауау" or "".join(a) == "оуоуа":
        print(i)