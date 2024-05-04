def f(n):
    s1, s2, s3, s4, s5 = str(n)
    a1 = int(s1) + int(s3) + int(s5)
    a2 = int(s2) + int(s4)
    return str(max(a1, a2)) + str( min( a1, a2))


for i in range (10000, 100000):
    if f(i) == "621":
        print(i)
        break