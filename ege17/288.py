a = [int(x) for x in open("17data/17-288.txt")]
c = []
d = min([x for x in a if x % 21 == 0])
for i in range(len(a)- 2):
    if abs(a[i]) % 7 != abs(a[i+1]) % 7 and abs(a[i]) % 7 != abs(a[i+2]) and abs(a[i+1]) % 7 != abs(a[i+2]):
        if a[i] < 0 or a[i+1] < 0 or a[i+2] < 0:
            c.append(max(a[i:i+3]) - min(a[i:i+3]))


print(len(c), min(c))