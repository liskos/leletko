file = open("26data/26-59.txt")
n = int(file.readline())
print(n)
a = []
for i in range(n):
    x,y = file.readline().split()
    a.append([int(x),int(y)])
a.sort()
b = []
for i in range(len(a)-1):
    for j in range(1,len(a)):
        if a[i][0] == a[j][0] and a[j][1] - a[i][1] == 3:
            b.append([a[i][1]+1,a[i+1][0]])
b.sort()
print(b[0][::-1])