import fnmatch
a = int("ba",16)
for i in range(132587371194,10**12,a):
    if fnmatch.fnmatch(str(hex(i)[2:]),"1?DED?BABA"):
        print(i,i//a)