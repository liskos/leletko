def prime_numbers(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    b = [i for i in range(n) if prime[i]]
    return b

f = []
r = prime_numbers((336492+1)//2)
for i in range(268312,336492+1):
    for x in r:
        if i % x == 0 and x**2 != i and (i // x) in r:
            f.append(i)
            break
print(len(f), min(f))