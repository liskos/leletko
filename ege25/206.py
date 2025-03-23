import fnmatch

for i in range(103456696,2*10**8,17):
    if fnmatch.fnmatch(str(i),"1?34567?9"):
        print(i,i//17)