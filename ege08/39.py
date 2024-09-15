import itertools
b = set()
for i, a in enumerate(itertools.product("abcdx", repeat=4), 1):
    if "".join(a).count("x") == 1:
        b.add(i)
print(len(b))