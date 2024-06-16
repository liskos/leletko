def f(n):
    n = str(n)
    s1, s2 = 0, 0
    for i in range(len(n)):
        if int(n[i]) % 2 == 0:
            s1 += int(n[i])
        if i % 2 != 0:
            s2 += int(n[i])
    return abs(s1-s2)


for i in range(1, 10000000):
    if f(i) == 29:
        print(i)
print(f(1234))