def f(n):
    n = str(n)[::-1]
    s1 = 0
    for i in range(16):
        if i % 2 != 0:
            if int(n[i]) * 2 >= 10:
                d = int(n[i]) * 2
                d = int(str(d)[0]) + int(str(d)[1])
                s1 = s1 + d
            else:
                s1 = s1 + int(n[i]) * 2
        if i % 2 == 0:
            s1 += int(n[i])
    return s1


for i in range(1234567891011122, 100000000000000000000000):
    if f(i) % 10 == 0:
        print(i)
        break
print(f(1234567891011121))