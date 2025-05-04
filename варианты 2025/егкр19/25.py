import fnmatch

for x in range(7993,10**10+1,7993):
    if x % 7993 == 0 and fnmatch.fnmatch(str(x),"4*4736*1"):
        print(x,x//7993)