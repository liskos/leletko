def f(x,y):
    if str(x)[0] == str(y)[0]:
        return True
    else:
        return False


for a in range(1,1000):
    if all( not(not f(x,28) and f(x,47)) or (x > (a - 20)) for x in range(1000)):
        print(a)