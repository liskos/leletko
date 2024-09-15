import itertools

for i, a in enumerate(itertools.product("опрт", repeat=5), 1):
    if "".join(a) == "топор" or "".join(a) == "ропот":
        print(i)


