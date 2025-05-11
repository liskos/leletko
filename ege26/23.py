file = open("26data/26-k3.txt")
n,k,m = map(int,file.readline().split())
print(n,k,m)
a = [int(file.readline()) for _ in range(n)]
a.sort(reverse=True)
print(a[k+m-1])
print(a[k-1])
