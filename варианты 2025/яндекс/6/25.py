def delit(n):
    a = set()
    for i in range(2,int(n**0.5+1)):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a


def k(n):
    d = delit(n)
    if d:
        return max(d) + min(d), d
    else:
        return 0, d

x = 0
for i in reversed(range(650000+1,656400)):
    t, d  = k(i)
    if len(d) == 6 and len(str(t)) == 4:
        x += 1
        print(i, t)
        if x == 5:
            break
    if i % 100000 == 0:
        print(i, "done")