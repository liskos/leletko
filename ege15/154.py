for a in range(1,1000):
    if all( not(x & 94 != 0) or (not(x&21 == 0) or (x & a != 0))  for x in range(1000)):
        print(a)
        break