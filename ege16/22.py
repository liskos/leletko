def F( n ):
    global a
    a += 1
    if n >= 1:
        a += 1
        F(n-1)
        F(n-2)
        a += 1


a = 0
F(35)
print(a)
