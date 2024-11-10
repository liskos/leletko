a = [int(x) for x in open("17data/17-288.txt")]
c = []
for i in range(len(a)- 2):
    if len(set(abs(x) % 7 for x in a[i:i+3])) == 3 and ((a[i] < 0) or (a[i+1] < 0) or (a[i+2] < 0)):
            c.append(max(a[i:i+3]) - min(a[i:i+3]))


print(len(c), min(c))