def f(n,m):
    return n%m == 0
b = [x for x in range(60,81)]
for a in range(1,1000):
    if all(f(x,a) or (not (x in b) or (not f(x,22))) for x in range(1000)):
        print(a)