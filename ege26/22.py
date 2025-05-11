file = open("26data/26-k2.txt")
n,k = map(int,file.readline().split())
a = [int(file.readline()) for _ in range(n)]
a.sort()
print(a[-51])
print(sum(a[k:-k])//(n-k*2))