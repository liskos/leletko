file = open("26data/26-j6.txt")
n = int(file.readline())
a = [int(x) for x in file]
a.sort(reverse=True)
b = a.copy()
s = sum(a)/10*9
k =0
i = 0
while sum(a) > s:
    a[i] = a[i]/10*8
    i += 1

g = [x for x in b[:i] if (sum(a) + x - (x/10*8) + (b[i]/10*8) - b[i]) <= s]
print(n-i,max(g))
