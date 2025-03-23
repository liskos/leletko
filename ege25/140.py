def devided(n):
    a = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n//i)
    return a
print(sorted(devided(18)))
for x in range(854321,1087654):
    d = devided(x)
    k = 0
    for i in range(len(d)-1):
        if abs(d[i] - d[i+1]) == 10:
            k += 1
    if k + 1 == len(d):
        print(x,d[0])