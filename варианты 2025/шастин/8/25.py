import fnmatch

for i in range(1984, 10**10,1984):
    if fnmatch.fnmatch(str(i),"?9?23?*23??"):
        if str(i)[0] in "2468" and str(i)[-2] in "13579" and str(i)[-1]  in "02468":
            print(i, i // 1984)