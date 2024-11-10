a = [int(x) for x in open("17data/17-276.txt")]
c = []
for i in range(len(a)- 2):
    s = abs(a[i]) + abs(a[i+1]) + abs(a[i+2])
    if s > 17043 and s % 3 == 0:
        c.append(sum(a[i:i+3]))
print(len(c), min(c))