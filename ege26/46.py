file = open("26data/26-46.txt")
n = int(file.readline())
a = [int(x) for x in file]
k = 0
m = 1000000000
for x in range(len(a)-2):
    for y in range(x+1,len(a)-1):
        for z in range(y+1,len(a)):
            if (a[x] + a[y] + a[z]) % 3 == 0 and ((a[x]+a[y]+a[z])/3) % 1 == 0 and (a[x]+a[y]+a[z])//3 in a:
                k += 1
                m = min(m,(a[x]+a[y]+a[z])//3)

print(k)
print(m)


