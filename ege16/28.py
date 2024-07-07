def F( n ):
    global b
    b = b + 2 * n + 1
    if n > 1:
        b = b + 3 * n - 8
        F(n-1)
        F(n-4)


b =  0
F(40)
print(b)
