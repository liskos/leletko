def devided(n):
    a = set()
    for i in range(1, (int(n ** 0.5) + 1)):
        if n % i == 0 and i % 2 == 1:
            a.add(i)
        if n % i == 0 and n // i % 2 == 1:
            a.add(n//i)
        if len(a) > 5:
            break
    return a

def prime_numbers(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    b = [i for i in range(n) if prime[i]]
    return b

pr = prime_numbers(88)
a = [i**4 for i in pr if i % 2 == 1]
b = []
for i in a:
    r = i
    while r < 55000000:
        r *= 2
    if 55000000 <= r <= 60000000:
        b.append(r)
for i in sorted(b):
    if len(devided(i)) == 5:
        print(i,max(devided(i)))
