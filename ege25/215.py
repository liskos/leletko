import fnmatch
def f(n):
    b = ""
    while n >0:
        b = b + str(n%3)
        n = n // 3
    return b[::-1]


for i in range(148,10**9,148):
    if fnmatch.fnmatch(f(i), "2?1?2?1?2?1"):
        print(i,i//148)