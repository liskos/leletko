import fnmatch

for i in range(21,10**9+1,21):
    if fnmatch.fnmatch(str(i), "1*5*9") and all(str(i)[x] < str(i)[x+1] for x in range(len(str(i))-1)):
        print(i,i//21)