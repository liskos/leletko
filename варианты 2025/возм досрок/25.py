import fnmatch

for i in range(154682,10**11+1,154682):
    if fnmatch.fnmatch(str(i), "*192?3*68"):
        print(i,i//154682)