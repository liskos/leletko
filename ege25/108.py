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
k = 0
m = 100000
r = prime_numbers(((315675+100)//2))
for i in range(238941,315675+1,):
    for x in r:
        for y in r:
            if x*y > i:
                break
            if x*y == i:
                k += 1
                if abs(x-y) >= m and abs(x-y) != 0:
                    m = abs(x-y)
                    h = [abs(x-y), x,y,i]
                    break

print(h[-1])