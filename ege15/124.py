def f(n,m):
    if n % m == 0:
        return True
    else:
        return False

for a in range(1,1000):
    if all( not f(x,18) or (not f(x,54) or f(x,a)) for x in range(1000)):
        print(a)