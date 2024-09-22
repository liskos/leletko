import itertools


def f(x, y, z, w):
    return (not x or y) and (y or z) and w


for a in itertools.product([0, 1], repeat=6):
    table = [(a[0], a[1], 0, 0), (0, 1, 0, a[2]), (0, a[3], a[4], a[5])]
    for p in itertools.permutations("xyzw"):
        if len(set(table)) == 3 and [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
            print("".join(p))