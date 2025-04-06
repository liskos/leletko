for a in range(1,1000):
    if all( not (x&102 != 0) or ( not(x & 36 == 0) or (x & a != 0)) for x in range(1000)):
        print(a)
        break