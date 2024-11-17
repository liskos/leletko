import fnmatch

def delet(n):
    """массив делителей числа"""
    a = []
    for i in range(1,int(n ** 0.5)+1):
        if n % i == 0:
            a.append(i)
            if i != n // i:
                a.append(n // i)
    return a


for i in range(993500,10**6+1):
    a = delet(i)
    if any(fnmatch.fnmatch(str(x), "1??56*5") for x in a):
        print(i, min([x for x in a if fnmatch.fnmatch(str(x), "1??56*5")]))