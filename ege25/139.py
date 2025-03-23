def devided(n):
    a = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.append([n//i,i])
    return a

for x in range(2000000,3000000):
    r = []
    for i in devided(x):
        if (i[0] - i[1]) <= 120:
            r.append([x,i[0]])
        if len(r) >= 3:
            print(x,r[0])