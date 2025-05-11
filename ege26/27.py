file = open("26data/26-J2.txt")
n = int(file.readline())
print(n)
a = [int(x) for x in file]
a.sort()
sr = sum(a)/n
m = a[len(a)//2]
k = 0
for i in a:
    if i <= m and i >= sr:
        k += 1
print(sr)
print(m)
print(k)