import itertools

def f(x, y, z, w):
    return (x or (not y)) and (not ( y == z)) and ( not w)


for a in itertools.product([0, 1], repeat=4):
    table =[(1, 1, a[0], a[1]), (a[2], 1, 0, 0), (1, a[3], 1, 0)]
    for p in itertools.permutations("xyzw"):
        if len(set(table)) == 3 and [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
            print("".join(p))