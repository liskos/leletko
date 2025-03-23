def devided(n):
    a = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.append([n//i,i])
    return a

print(devided(18))
k = 0
for x in range(500000,1000000):
    r = []
    for i in devided(x):
        if (i[0] - i[1]) <= 90:
            r.append([x,i[0]])
        if len(r) >= 3:
            print(x,r[0])