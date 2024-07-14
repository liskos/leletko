def F(n):
    if n>0:
        d=n % 10 + F(n//10)
        return d
    else: return 0

print(F(10))
for i in range(1, 100000):
    if F(i) > 32:
        print(i, F(i))
        break