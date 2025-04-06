def f(n):
    for i in range(2,n+1):
        if n % i == 0:
            return i + (n // i)
    return 0

k = 0
for i in range(900000):
    if k == 7:
        break
    if str(f(i))[-1] == "7" and str(f(i))[0] == "7":
        k += 1
        print(i,f(i))