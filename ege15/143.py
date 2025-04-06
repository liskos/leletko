def f(n,m):
    if n % m == 0:
        return True
    else:
        return False


for a in range(1,1000):
    if all( not(f(x,45) and (not f(x,15))) or (f(x,a)) for x in range(1000)):
        print(a)
        break