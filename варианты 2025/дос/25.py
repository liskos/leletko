a = [x for x in range(17,100000000,10)]
def f(n):
    global a
    k = 0
    i = 0
    while k == 0 and i < len(a):
        if n % a[i] == 0 and a[i] != n:
            k = a[i]
        i += 1
    return k

k = 0
for x in range(1125000,10**10):
    if k == 5:
        break
    if f(x) > 0:
        print(x,f(x))
        k += 1