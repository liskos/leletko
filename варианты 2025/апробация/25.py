def f(n):
    r = []
    for i in range(2,n):
        if n % i == 0:
            r.append(i)
    return sum(r)

k = 0
print(f(20))
for i in range(500000,10**10):
    if f(i) % 10 == 9 and k < 5:
        print(i, f(i))
        k += 1

