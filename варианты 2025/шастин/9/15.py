def f(a,b):
    return a % b

for a in range(1,1000):
    if all((a+2 * x > 400 - a) and (f(a,100) + f(120,a) > 140) for x in range(1, 1000)):
        print(a)
        break