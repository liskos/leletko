for a in range(1,1000):
    if all( not(x&a!=0) or (not(x&14==0) or (x&75!=0))  for x in range(1000)):
        print(a)