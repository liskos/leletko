def prime_numbers(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2,n):
        if prime[i]:
            for j in range(i**2, n, i):
                prime[j] = False
    b = [i for i in range(n) if prime[i]]
    return b


r = prime_numbers(20222022+1)
for i in range(121332132+1,20222022,-1):
    for x in r:
        if i % x == 0 and (i // x) in r and min(x,i//x) > 999 :
            print(i,min(x,i//x))
            break