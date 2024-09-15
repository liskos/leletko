import itertools

for i, a in enumerate(itertools.product("ьсоне", repeat=4), 1):
    if i == 100:
        print(a)
        break
