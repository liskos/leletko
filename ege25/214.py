import fnmatch
a = int("101101",2)
for i in range(a,10**9,a):
    if fnmatch.fnmatch(bin(i)[2:], "1?1?1?1?1??1"):
        print(i,i//a)
