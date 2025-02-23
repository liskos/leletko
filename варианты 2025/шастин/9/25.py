def r(n):
    global p
    a = []
    for i in p:
        if n % i == 0:
            a.append(i)
    return max(a) - min(a)

def prime_numbers():
    n = 2000000
    a = [True] * n
    a[0] = a[1] = False
    for i in range(2, n):
        if a[i]:
            for j in range(i*i, n, i):
                a[j] = False
    return [i for i in range(n) if a[i]]

p = prime_numbers()
k = 0
for i in range(3333338, 10**10):
    raz = r(i)
    if raz > 1000 and raz % 3 == 0:
        k += 1
        print(i,raz)
        if k == 5:
            break