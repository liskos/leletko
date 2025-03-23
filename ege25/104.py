def prime_numbers(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    b = [i for i in range(n) if prime[i]]
    return b

f = []
r = prime_numbers((473265+1)//2)
for i in range(412567,473265+1):
    for x in r:
        if i % x == 0 and x**2 != i and (i // x) in r:
            f.append(i)
            break
h = 0
m = 100000
sr = sum(f) / len(f)
for i in f:
    if abs(sr - i) < m:
        m = abs(sr - i)
        h = i
print(len(f), h)