a = [int(x) for x in open("17data/17-296.txt")]
c = []
m = max(a)
s = [int(str(abs(x))[0]) for x in a]
for i in range(len(a)- 1):
    if a[i] * a[i+1] > sum(s):
        c.append(a[i]+a[i+1])
print(len(c), max(c))