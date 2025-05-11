file = open("26data/26-k5.txt")
n,k,m = map(int,file.readline().split())
a = [int(x) for x in file]
a.sort(reverse=True)
print(a[m-1])
print(sum(a[-k:])//k)