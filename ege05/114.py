def f(n):
    s1, s2, s3, s4,  = str(n)
    a1 = int(s1) + int(s2)
    a2 = int(s2) + int(s3)
    a3 = int(s3) + int(s4)
    b = [a1, a2, a3 ]
    b =  sorted(b)
    return str(b[1]) + str(b[2])


for i in range (1000, 10000):
    if f(i) == "210":
        print(i)
