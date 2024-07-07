def F( n ):
    global b
    b = b + n * n
    if n > 1:
        b = b + 2 * n + 1
        F(n-2)
        F(n//3)

b = 0
F(199)
print(b)