import fnmatch

for i in range(169,10**9,169):
    if fnmatch.fnmatch(str(i),"123*567?"):
        print(i, i // 169)