import itertools

for i, a in enumerate(itertools.product("аоу",repeat=5),1):
    if "".join(a) == "оаоао":
        print(i,a)