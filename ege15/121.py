def f(n,m):
    if n % m == 0:
        return True
    else:
        return False

for a in range(1,1000):
    if all( not(not f(x,a) and f(x,21)) or (not f(x,14)) for x in range(1000)):
        print(a)