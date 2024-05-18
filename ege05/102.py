def f(x):
    s1 = x % 4
    s2 = x % 2
    s3 = x % 3
    return str(s1) + str (s2) + str(s3)


for i in range (10, 100):
    if f(i) == "311":
        print(i)
