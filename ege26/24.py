file = open("26data/26-k4.txt")
n,k = map(int,file.readline().split())
a = [int(x) for x in file]
a.sort(reverse=True)
print(sum(a[k:k*2])//k)
print(sum(a[:k])//k)