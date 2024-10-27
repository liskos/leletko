a = [int(x) for x in open("17data/17-5.txt")]
r = []
k = 0
for i in range(len(a) -1):
    if str(a[i])[-1] == '7' or str(a[i+1])[-1] == "7":
        r.append(a[i] + a[i + 1])
print(len(r), max(r))