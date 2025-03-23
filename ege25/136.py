def prime_numbers(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    b = [i for i in range(n) if prime[i]]
    return b


d = prime_numbers(100000)
def f(n):
     global d
     r = []
     i = 2
     while len(r) < 6 and i < n **0.5:
         if n % i == 0 and i in d:
             r.append(i)
         i += 1
     return r


for i in range(25317,51237):
    if len(f(i)) >= 6:
        print(i, max(f(i)), f(i))
