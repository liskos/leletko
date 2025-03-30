import fnmatch, time

def prime_numbers(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    b = [i for i in range(n) if prime[i]]
    return b

def s(n):
    global p
    a = []
    i = 0
    while n > 1:
        if n % p[i] == 0:
            a.append(str(p[i]))
        while n % p[i] == 0:
            n = n // p[i]
        i += 1
    return a

def s1(n):
    global p1
    for i in p1:
        if n % i == 0:
            return i


t1 = time.time()
k = 0
p = prime_numbers(2400000)
p1 = [i for i in p if str(i)[:2] == "10"]
for i in range(2352001, 10**10):

    if fnmatch.fnmatch(str(s1(i)), "10*"):
        b = s(i)
        c = "".join(b)
        if fnmatch.fnmatch(c, "10*29"):
            print(i,b[-1])
            k += 1
            if k == 5:
                break
print(time.time()-t1)