import fnmatch

for i in range(17,10**9+1,17):
    if fnmatch.fnmatch(str(i), "12345?6?8"):
        print(i,i//17)