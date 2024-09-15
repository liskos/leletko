import itertools
b = 0
for i, a in enumerate(itertools.product("щогба", repeat=6), 1):
    s = "".join(a)
    if s == "общага":
        print(i)

