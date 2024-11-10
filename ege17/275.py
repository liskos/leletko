a = [int(x) for x in open("17data/17-275.txt")]
c = []
for i in range(len(a)- 1):
    if abs(a[i] + a[i+1]) % 11 == 0:
        c.append(sum(a[i:i+2]))
print(len(c), max(c))