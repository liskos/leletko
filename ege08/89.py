import itertools
b = 0
for i, a in enumerate(itertools.product("110г", repeat=6), 1):
    s = "".join(a)
    if s[0] == "1" and s[-1] == "г":

        b = b + 1
print(b)