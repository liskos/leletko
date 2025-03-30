def prime_numbers(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    b = [i for i in range(n) if prime[i]]
    return b
def f(n):
    p = 1
    while n >0:
        p = p * n
        n = n - 1
    return p

def su(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s

r = prime_numbers(10000000000)
for i in  range(2,12+1):
    g = []
    for x in r:
        if f(i) % x == 0 and x % 2 != 0:
            g.append(x)
    if len(g) % 2 == 0:
        print(i,len(g)+1)