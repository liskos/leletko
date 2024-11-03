import itertools

k = []
for i, a in enumerate(itertools.product("аекптч", repeat=7), 1):
    s = "".join(a)
    if s == "аптечка" or s == "печатка":
        k.append(i)

print(max(k)- min(k) - 1)