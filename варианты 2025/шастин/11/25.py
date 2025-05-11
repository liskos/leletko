def prime_numbers(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    b = [i for i in range(n) if prime[i]]
    return b

k = 0
gh = prime_numbers(750000)
for i in range(750000,1,-1):
    r = []
    for x in gh:
        if i % x == 0 and x % 10 == 7:
            r.append(x)
    if r:
        f = sum(r)//len(r)
        if f != 0 and f % 111 == 0:
            print(i,f)
            k += 1
        if k == 5:
            break