import itertools
b = 0
for i, a in enumerate(itertools.product("110", repeat=6), 1):
    s = "".join(a)
    if s[0] == "1":
        b = b + 1
print(b)