file = open("26data/26-55.txt")
n,s = map(int,file.readline().split())
print(n)
print(s)
a = [int(x) for x in file]
a.sort(reverse=True)
b = []
k = 0
mm = []
while len(a) > 0:
    temp = []
    b.append([])
    for x in a:
        if x + sum(b[-1]) <= s:
            b[-1].append(x)
        else:
            temp.append(x)
    a = temp
print(len(b), sum(b[-1]))


