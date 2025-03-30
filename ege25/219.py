import fnmatch

def prime_numbers(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    b = [i for i in range(n) if prime[i]]
    return b

print(prime_numbers(2234566)[:1000])
for i in range(2367803,10**10):
    print(i)
    r = prime_numbers(i)
    b = ""
    for x in r:
        b = b + str(x)
    if fnmatch.fnmatch(b, "10*29"):
        print(i,max(r))