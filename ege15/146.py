def f(n,m):
    if n % m == 0:
        return True
    else:
        return False


for a in range(1,1000):
    if all( not(f(x,15) and (not f(x,21))) or (not f(x,a) or (not f(x,15)))   for x in range(1000)):
        print(a)
        break