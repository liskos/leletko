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
r = prime_numbers(((305283+100)//2))
for i1 in range(len(r)- 2):
    for i2 in range(i1+1,len(r)-1):
        if i1 * i2 > 305283+1:
            break
        for i3 in range(i2+1,len(r)):
            g = r[i1] * r[i2] * r[i3]
            if g > 305283+1:
                break
            if 236228 <= g <= 305283+1:
                h.append(g)

print(len(h), sum(h)/len(h))