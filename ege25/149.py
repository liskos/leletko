def devided(n):
    a = set()
    k = 0
    for i in range(1, (int(n ** 0.5) + 1)):
        if len(a) > 5:
            break
        if n % i == 0 and i % 2 != 0:
            k += 1
            a.add(i)
        if (n // i) % 2 == 1 and n % i == 0:
            a.add(n//i)
            k += 1
    return a

print(devided(55383364))
for i in range(55000000,60000000+1):
    if len(devided(i)) == 5:
        print(i,max(devided(i)))
