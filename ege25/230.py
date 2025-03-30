def prime_numbers(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    b = [i for i in range(n) if prime[i]]
    return b

def prim_del(n):
    global p
    a = set()
    for i in p:
        if n % i == 0:
            a.add(i)
    return a


p = prime_numbers(100)
for i in  reversed(range(2,14+1)):
    g = set()
    for i in range(2, i+1):
        g |= prim_del(i)
    if len(g) % 2 == 1:
        print(i,len(g))