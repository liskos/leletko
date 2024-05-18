def f(x):
    s1 = x % 2
    s2 = x % 3
    s3 = x % 5
    return str(s1) + str (s2) + str(s3)


for i in range (10, 100):
    if f(i) == "122":
        print(i)