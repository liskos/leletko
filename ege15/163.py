for a in range(1,1000):
    if all( not((x&13!=0) and (x&39!=0)) or ((x&a!=0) and (x&13!=0))  for x in range(1000)):
        print(a)
        break