import fnmatch
k = 0
for s in open("24data/24-s1.txt"):
    if fnmatch.fnmatch(s,"*Z?RO*"):
        k +=1

print(k)