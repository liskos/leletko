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
m = 10000000
r = prime_numbers((578925+1)//2)
for i in range(523456,578925+1):
    for x in range(int(i**0.5)-30,int(i**0.5)+30):
        for y in range(int(i**0.5)-30,int(i**0.5)+30):
            if x*y == i and x in r and y in r:
                if abs(x-y) < m and abs(x-y) != 0:
                    m = abs(x-y)
                    print(abs(x-y),x,y,i)


