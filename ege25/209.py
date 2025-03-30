def prime_numbers(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    b = [i for i in range(n) if prime[i]]
    return b

g = prime_numbers(10**7)

a = [2**i for i in range(1,21)]
print(a)

for x in range(99999,1048571+1):
    for y in a:
        if abs(x - y) <= 5 and x in g:
            print(x,y)