def prime_numbers(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    b = [i for i in range(n) if prime[i]]
    return b

pr = prime_numbers(100000)
for i in range(2, 10**10):
    k_del = 1
    r = i
    for p in pr:
        k = 1
        while r % p == 0:
            k += 1
            r //= p
        k_del = k_del * k
        if r == 1:
            break
    if k_del == 1600:
        print(i)
        break
    if i % 100000 == 0:
        print(i, "ok")