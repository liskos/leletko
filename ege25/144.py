def prime_numbers(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    b = [i for i in range(n) if prime[i]]
    return b
a = prime_numbers(60000)
for i in range(33333,55555):
    r = []
    for x in a:
        if i % x == 0 and x != 1 and x != i:
            r.append(x)
    if len(r) > 0:
        if i % sum(r) == 0 and sum(r) > 250:
            print(i,sum(r))
