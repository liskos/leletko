def f(n):
    s1, s2, s3, = str(n)
    b = [s1, s2, s3]
    b = sorted(b)
    a1 = str(b[0]) + str(b[1])
    a2 = str(b[2]) + str(b[1])
    return int(a2) - int(a1)


for i in range(100, 1000):
    if f(i) == 50:
        print(i)
print(f(351))