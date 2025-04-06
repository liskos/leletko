def f(n,m):
    if n % m == 0:
        return True
    else:
        return False


for a in range(1,1000):
    if all( not (not f(x,a)) or (not f(x,24) and (not f(x,36)))  for x in range(1000)):
        print(a)
