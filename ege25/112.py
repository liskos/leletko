def prime_numbers(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    b = [i for i in range(n) if prime[i]]
    return b

o = 0
h = []
m = 10000000
r = prime_numbers(((363249+100)//2))
for i1 in range(len(r)- 1):
    for i2 in range(i1+1,len(r)):
        g = r[i1] * r[i2]
        if g > 363249+1:
            break
        if 298435 <= g <= 363249+1:
            h.append(g)


for p in h:
    if abs((sum(h) / len(h)) - p) < m:
        m = abs((sum(h) / len(h)) - p)
        o = p

print(len(h), o)


