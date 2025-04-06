for a in range(1,1000):
    if all( not(x & 35 != 0) or (not (x & 31 == 0) or (x & a != 0))  for x in range(1000)):
        print(a)
        break