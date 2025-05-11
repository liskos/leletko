file = open("26data/26-J1.txt")
n = int(file.readline())
print(n)
a = [int(x) for x in file]
a.sort(reverse=True)
b = []
for i in range(n-1):
    for j in range(n-1,i,-1):
        if a[i] + a[j] == 100 and a[i] != 0 and a[j] != 0:
            b.append(a[i]+a[j])
            a[j] = 0
            break

print(len(b))