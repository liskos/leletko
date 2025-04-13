import fnmatch

for i in range(10**7,1,-1):
    if str(i)[0] == "8":
        if fnmatch.fnmatch(str(i), "89?45*75"):
            print(i,i//25)