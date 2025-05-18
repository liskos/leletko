file = open("26data/26-j8.txt")
n = int(file.readline())
a = [int(x) for x in file]
print(max(a)*0.6)
a.sort()
b = a.copy()
a = sum(a[:n//10*7])*0.7 + sum(a[n//10*7:])*0.6
b = sum(b[:n//2])*0.6 + sum(b[n//2:])*0.65
print(int(max(a,b)- min(a,b)))

