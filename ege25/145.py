def f(n):
    s = 0
    while n> 0:
        s = s + n % 10
        n = n // 10
    return s

def devided(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return a

r = []
for i in range(1000000,1300000):
    s = str(i)
    if s.count("3") == s.count("4") == s.count("5") == s.count("6") == s.count("7") == s.count("8") == s.count("9") == 0:
        if f(i) % 10 == 0:
            r.append(i)

for i in range(1,len(r)//10+1):
    print(r[i*10-1],len(devided(r[i*10-1]))-2)

