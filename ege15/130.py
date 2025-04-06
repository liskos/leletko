def f(n,m):
    if n % m == 0:
        return True
    else:
        return False

for a in range(1,1000):
    if all( not (f(x,a) and (not f(x,16))) or f(x,23)  for x in range(1000)):
        print(a)
        break