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
h = []
m = 0
r = prime_numbers(((309876+100)//2))
for i in range(237981,309876+1,):
    for x in r:
        if i % x == 0 and (i // x) in r and str(x)[-1] == str(i//x)[-1]:
            h.append(i)
            break

print(len(h), max(h))