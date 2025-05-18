file = open("26data/26-47.txt")
n = int(file.readline())
a = [int(x) for x in file]
vk = 0
km = 0
for x in range(len(a)-1):
    for y in range(x+1,len(a)):
        sr = (a[x] + a[y])/2
        k = 0
        for i in a:
            if i < sr:
                k += 1
        if k !=0 and k % 100 == 0:
            vk += 1
            km = max(k,km)

print(vk,km)