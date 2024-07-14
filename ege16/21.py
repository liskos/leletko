def F( n ):
    global a
    a += 1
    if n >= 1:
        a += 1
        F(n-1)
        F(n-2)

for i in range(1, 1000):
    a = 0
    F(i)
    if a > 2400000
a = 0

print(a)