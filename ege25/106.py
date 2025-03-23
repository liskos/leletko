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
r = prime_numbers(((684934+100)//2))
for i in range(631632,684934+1,):
    for x in r[:40]:
        for y in r[-40:]:
            if x * y == i and x != y:
                if abs(x-y) >= m:
                    m = abs(x-y)
                    print(abs(x-y),x,y,i)
