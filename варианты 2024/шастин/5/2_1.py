def f(x,y,z,w):
    return (( not x) and (not z or y) and ( not w)) or ((z == w) and (( not(x or y)) or w))


import itertools
for a in itertools.product([0,1], repeat = 4):
    table = [(1, 0, 0, 0), (a[0], 1, 0, a[1]), (1, 0, a[2], a[3])]
    for p in itertools.permutations("xyzw"):
        if len(set(table)) == 3 and [f(**dict(zip(p, t))) for t in table]== [1,1,1]:
            print(p)