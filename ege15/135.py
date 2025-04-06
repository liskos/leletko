def f(n,m):
    if n % m == 0:
        return True
    else:
        return False

for a in range(1,1000):
    if all( not f(x,a) or (f(x,14) and f(x,21)) for x in range(1000)):
        print(a)
        break