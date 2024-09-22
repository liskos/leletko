def f(x, y, z, w):
    return (x or y) and ( y != z) and ( not w)


import itertools
for a in itertools.product([0, 1], repeat=4):
    table = [(a[0], 1, a[1], 1), (0, 0, 1, a[2]), (0, a[3], 1, 1)]
    for p in itertools.permutations("xyzw"):
        if len(set(table)) == 3 and [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
            print("".join(p))
