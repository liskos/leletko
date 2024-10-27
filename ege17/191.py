a = [int(x) for x in open("17data/17-7.txt")]
r = []
k = 0
for i in range(len(a) -2):
    if hex(a[i])[-1] == "9" and hex(a[i])[-1] != "a9":
        r.append(min(a[i], a[i+1], a[i+2]))
print(len(r), max(r))