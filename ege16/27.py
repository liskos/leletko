def F( n ):
    global b
    b = b + n + 1
    if n > 1:
        b = b + n * 2
        F(n-1)
        F(n-3)

b = 0
F(30)
print(b)