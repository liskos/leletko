def s(n):
    s = 0
    while n> 0:
        s = s + n % 10
        n = n // 10
    return s

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
    if i in a and s(i) > 35:
        print(i,s(i))