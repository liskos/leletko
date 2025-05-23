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
r = prime_numbers(((502439+100)//2))
for i1 in range(len(r)- 1):
    for i2 in range(i1+1,len(r)):
        g = r[i1] * r[i2]
        if g > 502439+1:
            break
        if 478392 <= g <= 502439+1:
            h.append([abs(r[i1] - r[i2]), g, r[i1],r[i2]])

print(len(h), min(h)[1])