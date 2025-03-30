import fnmatch
a = int(str(79),16)
for i in range(a,10**12,a):
    if fnmatch.fnmatch(str(hex(i)[2:]),"1?DED?CED"):
        print(i,i//a)