def f(n):
    s1, s2, s3, s4 = str(n)
    a1 = int(s1) + int(s4)
    a2 = int(s2) + int(s3)
    return str(max(a1, a2)) + str( min( a1, a2))


for i in range (1000, 10000):
    if f(i) == "128":
        print(i)
        break
