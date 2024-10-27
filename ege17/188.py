a = [int(x) for x in open("17data/17-7.txt")]
r = []
k = 0
for i in range(len(a) -2):
    k = 0
    if hex(a[i])[-1] == "0":
        k = k + 1
    if hex(a[i+1])[-1] == "0":
        k += 1
    if hex(a[i + 2])[-1] == "0":
        k += 1
    if k >= 2:
        r.append(max(a[i], a[i+1], a[i+2]))
print(len(r), sum(r))