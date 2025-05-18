file = open("26data/26-j7.txt")
n = int(file.readline())
a = [int(x) for x in file]
a.sort(reverse=True)
b = a[:n//10*2]
print(int(sum(b)/10*8))
vs = sum(a)/10*6
v = vs - sum(b)/10*8
print(min(a)*(v/sum(a[n//10*2:])))