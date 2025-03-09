import fnmatch
k = 0
for i in range(111,10**8,111):
    if fnmatch.fnmatch(str(i), "3*4?5*6?") and i % 2 == 0:
        k += 1
print(k)