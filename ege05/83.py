def f(n):
    s1, s2, s3,  = str(n)
    a1 = int(s1) + int(s2)
    a2 = int(s2) + int(s3)
    return str(min(a1, a2)) + str( max( a1, a2))


for i in range (100, 1000):
    if f(i) == "1115":
        print(i)
        break