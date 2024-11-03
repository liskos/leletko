a = [int(x) for x in open("17data/17-10.txt")]
r = []
for i in range(len(a) -1):
    s = str(a[i] + a[i+1])
    if len(s) == 3 and int(s[-1]) > int(s[-2]):
        r.append(int(s))

print(len(r), min(r))