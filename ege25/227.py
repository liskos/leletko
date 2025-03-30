def prime_numbers(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    b = [i for i in range(n) if prime[i]]
    return b


for i in range(200,2022+1):
    r = prime_numbers(i)
    for x in range(len(r)-1):
        for y in range(x,len(r)):
            if r[x] * r[y] == i and r[x] > 10:
                print(i,r[x])