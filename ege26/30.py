file = open("26data/26-J5.txt")
n = int(file.readline())
a = [int(x) for x in file]
print(a)
b = [a[0]]
for i in range(1,n-1):
    sosedi = sorted(a[i-1:i+2])
    b.append(sosedi[1])
b.append(a[-1])
s = 0
for i in range(n):
    if a[i] > b[i]:
        s = s + a[i] - b[i]

k = len([x for x in b if x == min(b)])
print(k,s)
