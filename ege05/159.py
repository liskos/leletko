for n in range(0,256):
    r = bin(n)[2:]
    r = 11111111 - int(r)
    r = int(str(r),2)
    r = r - n
    if r == 45:
        print(n)
