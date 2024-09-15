import itertools

for i, a in enumerate(itertools.product("иоу", repeat=5), 1):
    if i == 240:
        print("".join(a))
        break