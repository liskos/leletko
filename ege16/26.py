def F( n ):
    global b
    b = b + n+1
    if n > 1:
        b = b + n + 5
        F(n-1)
        F(n-2)

b = 0
F(24)
print(b)

