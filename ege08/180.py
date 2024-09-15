import itertools
b = 0
for i, a in enumerate(itertools.product("мечта", repeat=6), 1):
    s = "".join(a)
    if s.count("а") >= 3:
        b += 1
print(b)
