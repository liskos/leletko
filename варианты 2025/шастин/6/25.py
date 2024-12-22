import fnmatch
for i in range(2025,10**10,2025):
    if fnmatch.fnmatch(str(i), "33?2*42?") and fnmatch.fnmatch(str(i), "*32??2?"):
        print(i,i//2025)