a = [int(x) for x in open("17data/17-274.txt")]
c = []
for i in range(len(a)- 1):
    s = abs(a[i]) + abs(a[i+1])
    if s > 17043 and s % 3 == 0:
        c.append(sum(a[i:i+2]))
print(len(c), min(c))